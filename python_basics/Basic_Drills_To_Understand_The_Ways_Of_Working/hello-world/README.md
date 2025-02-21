

# Say Helloo

A simple Python package to demonstrate publishing on TestPyPI.

## Installation

To install the package from TestPyPI, run:

```
pip install -i https://test.pypi.org/simple/ say_helloo
```

## Usage

Import and use the package:

```python
from hello_world.say_hello import say_hello

say_hello()
```

## Poetry Commands

### Check Virtual Environment
```sh
poetry env info
```

### Show Installed Packages
```sh
poetry show
```

### Show Specific Package Info
```sh
poetry show say_helloo
```

### Run Python Inside Virtual Environment
```sh
poetry run python
```

### Run a Python Script
```sh
poetry run python -c "import say_helloo; print(say_helloo.__name__)"
```

### Add a Dependency
```sh
poetry add <package_name>
```

### Remove a Dependency
```sh
poetry remove <package_name>
```

### Update Dependencies
```sh
poetry update
```

