#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
import traceback
from pathlib import Path

from cdp_data import CDPInstances, keywords
import numpy as np

###############################################################################

FILEPATH = Path(__file__)


class Args(argparse.Namespace):
    def __init__(self) -> None:
        self.__parse()

    def __parse(self) -> None:
        p = argparse.ArgumentParser(
            prog="generate-ngram-data",
            description=(
                "Generate ngram usage data to be stored and prepared for import in "
                "the JavaScript Living Paper. "
                "Defaults to storing frequencies for 2022-03-01 to 2022-07-01."
            ),
        )
        p.add_argument(
            "-o",
            "--outfile",
            default=FILEPATH.parent.parent / "data/ngram-histories.csv",
            type=Path,
            help="Optional path for where to place the parquet file.",
        )
        p.add_argument(
            "-s",
            "--start_datetime",
            dest="start_datetime",
            default="2022-03-01",
            help="Optional ISO formatted datetime string to use as the start datetime."
        )
        p.add_argument(
            "-e",
            "--end_datetime",
            dest="end_datetime",
            default="2022-07-01",
            help="Optional ISO formatted datetime string to use as the start datetime."
        )
        p.add_argument(
            "--debug",
            action="store_true",
            help="Run with debug logging",
        )
        p.parse_args(namespace=self)


###############################################################################

def _generate_ngram_history(
    outfile: Path,
    start_datetime: str,
    end_datetime: str,
) -> Path:
    # Get dataset and compute frequencies
    ngram_usage = keywords.compute_ngram_usage_history(
        CDPInstances.Seattle,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
    )

    # Convert date to timestamp
    ngram_usage["session_date"] = ngram_usage["session_date"].apply(
        lambda dt: dt.isoformat()
    )

    # Subset columns
    # Optional: Can add "infrastructure"
    subset = ngram_usage[["ngram", "day_ngram_percent_usage", "session_date"]]

    # We don't need so much precision, reduce to float32
    subset = subset.astype({
        "day_ngram_percent_usage": np.float32,
    })

    # Store and return
    subset.to_csv(outfile, index=False)
    return outfile

def main() -> None:
    try:
        args = Args()

        # Handle logging
        if args.debug:
            log_level = logging.DEBUG
        else:
            log_level = logging.INFO
        
        logging.basicConfig(
            level=log_level,
            format="[%(levelname)4s: %(module)s:%(lineno)4s %(asctime)s] %(message)s",
        )
        log = logging.getLogger(__name__)

        # Compute
        _generate_ngram_history(
            outfile=args.outfile,
            start_datetime=args.start_datetime,
            end_datetime=args.end_datetime,
        )
        log.info(f"Stored ngram history to: {args.outfile}")
    except Exception as e:
        log.error("=============================================")
        log.error("\n\n" + traceback.format_exc())
        log.error("=============================================")
        log.error("\n\n" + str(e) + "\n")
        log.error("=============================================")
        sys.exit(1)

# Allow running this file alone
if __name__ == "__main__":
    main()