# README.md

## Hello World and Many Hellos Projects

This repository contains two Python projects: `hello_world` and `many_hellos`. The `hello_world` project is a simple library that provides a function to say hello, while the `many_hellos` project is a command-line application that uses the `hello_world` library to greet multiple people.

### Project Structure

- **hello_world/**: The library that contains the `say_hello` function.
  - `say_hello.py`: The main module that exports the `say_hello` function.
  - `config_reader.py`: A module that handles loading configuration from a YAML file.
  - `_config.yaml`: A default configuration file shipped with the library.

- **many_hellos/**: The command-line application that uses the `hello_world` library.
  - `cli.py`: The main script that implements the command-line interface using `typer`.

### Installation

1. **Install the `hello_world` library:**

   You can install the `hello_world` library from dev-pypi using pip:

   ```bash
   pip install --index-url https://test.pypi.org/simple/ hello_world
   ```

2. **Install the `many_hellos` CLI:**

   Clone this repository and install the `many_hellos` CLI:

   ```bash
   git clone <repository-url>
   cd many-hellos
   pip install .
   ```

### Usage

#### `hello_world` Library

The `hello_world` library provides a `say_hello` function that greets a person by their name. The function can be configured using a `_config.yaml` file to repeat the greeting multiple times.

**Example Usage:**

```python
from hello_world.say_hello import say_hello

print(say_hello("Alice"))
```

#### `many_hellos` CLI

The `many_hellos` CLI allows you to greet multiple people at once. It uses the `say_hello` function from the `hello_world` library.

**Example Usage:**

```bash
many-hellos hello Alice Bob Charlie
```

### Configuration

The `say_hello` function can be configured using a `_config.yaml` file. The configuration file should be placed in the current working directory or specified using the `CONFIG_PATH` environment variable.

**Example `_config.yaml`:**

```yaml
num_times: 3
```

This configuration will make the `say_hello` function repeat the greeting 3 times.

### Logging

The library and CLI both use Python's `logging` library for logging. You can control the logging level using the `logging.basicConfig` function.

**Example:**

```python
import logging

# Turn on logging for the entire application
logging.basicConfig(level=logging.INFO)

# Turn on logging only for the config reader
logging.getLogger("hello_world.config").setLevel(logging.INFO)
```
---
note: created using deepseek AI