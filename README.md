# cdp-data-interactive

[![CI](https://github.com/evamaxfield/cdp-data-interactive/actions/workflows/ci.yml/badge.svg)](https://github.com/evamaxfield/cdp-data-interactive/actions/workflows/ci.yml)

This repository stores the files needed for [quarto](https://quarto.org/) to generate a slightly modified, up-to-date, interactive version our [ASIS&T AM22 conference paper](https://arxiv.org/abs/2204.09110).

View the rendered article at: [https://evamaxfield.github.io/cdp-data-interactive/](https://evamaxfield.github.io/cdp-data-interactive/)

### Abstract

Large scale comparative research into municipal governance is often prohibitively difficult due to a lack of high-quality data.
Recent advances in speech-to-text algorithms and natural language processing techniques has made it possible to more
easily collect and analyze this type of data. In this paper, we introduce an open-source platform,
the Council Data Project (CDP), to curate novel datasets for research into municipal governance. The contribution of
this work is two-fold: 1. We demonstrate that CDP, as an infrastructure, can be used to assemble reliable comparative
data across municipalities; 2. We provide exploratory analysis to show how CDP data can be used to gain insight into how
municipal governments perform over time. We conclude by describing future directions for research on and with CDP such as
the development of machine learning models for speaker annotation, outline generation, and named entity recognition to
the linking of data for large-scale comparative research.

---

### Development Commands

```
just --list
Available recipes:
    build   # build page
    clean   # remove build files
    default # list all available commands
    setup name="cdp-data-interactive" # create conda env and install all deps
    watch   # watch file, build, and serve
```
