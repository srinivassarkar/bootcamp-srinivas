
!! POETRY CHEAT SHEET

-> INSTALLATION
!! Recommended Method (curl)
curl -sSL https://install.python-poetry.org | python3 -

!! Alternative Method (pip)
pip install poetry

!! Verify Installation
poetry --version

-> CREATING & MANAGING PROJECTS
!! Create a New Project
poetry new my_project

!! Install Existing Dependencies
poetry install

!! Add a Dependency
poetry add requests

!! Add a Development Dependency
poetry add --dev pytest

-> WORKING WITH VIRTUAL ENVIRONMENTS
!! Run a Script in Virtual Environment
poetry run python my_script.py

!! Activate Virtual Environment
poetry shell

!! Export Dependencies to requirements.txt
poetry export -f requirements.txt --output requirements.txt

-> MANAGING PACKAGES
!! Build a Package
poetry build

!! Publish to PyPI
poetry publish

!! Publish to TestPyPI
poetry publish --repository testpypi

-> CONFIGURATION & SETTINGS
!! Configure Virtual Environments in Project Directory
poetry config virtualenvs.in-project true

-> ADVANCED FEATURES
!! Add Dependency Groups
poetry add --group docs sphinx

!! Define CLI Tool
!! Add in pyproject.toml:
[tool.poetry.scripts]
my-cli = "my_project.cli:main"

!! Run CLI Tool
poetry run my-cli --name "Alice"



