# list all available commands
default:
  just --list

# clean all build, python, and lint files
clean:
	rm -fr _build

# create conda env and install all deps
setup name="cdp-data-interactive":
    conda env create -n {{name}} --file {{justfile_directory()}}/environment.yml

# Store various dirs and filepaths
CONTENT_DIR := justfile_directory() + "/src/"
PAPE_URI := CONTENT_DIR + "pape.qmd"

# watch file, build, and serve
watch:
    quarto preview {{PAPE_URI}} --to html

# build page
build:
    quarto render {{PAPE_URI}} -o index.html --to html