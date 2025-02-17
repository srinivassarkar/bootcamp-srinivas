# File Processing CLI

A CLI tool for processing text files using a customizable pipeline.

## TextTransform

**TextTransform** is a Python library for processing and transforming text files. It provides a variety of functions to manipulate text, including converting to uppercase, removing stop words, and more. The library is designed to be modular and extensible, allowing users to create custom processing pipelines.

## Features

- Convert text to uppercase
- Remove common stop words
- Capitalize words
- Fetch geographical information from IP addresses
- Stream processing of text records
- Customizable processing pipelines using YAML configuration

## Installation

Ensure you have [Poetry](https://python-poetry.org/) installed, then run:

```bash
poetry install
```

## Convert file content to uppercase
```
poetry run python commands.py basic input.txt --output-filename output.txt
```


## Convert file content to uppercase (default output: input.txt.processed)

```
poetry run python commands.py basic input.txt
```

## Apply transformations from pipeline.yaml
```
poetry run python -m commands dynamic input.txt
```

## Another example of basic processing with an explicit output filename
```
poetry run python commands.py basic input.txt --output-filename output.txt
```

---