<div class="container">

# Poetry Cheat Sheet – From Project Setup to Publishing

## 1\. Install & Configure Poetry

    curl -sSL https://install.python-poetry.org | python3 -

**Verify installation:**

    poetry --version

## 2\. Create & Set Up a New Project

    poetry new <package-name>

    cd <package-name>

    poetry init

## 3\. Managing Dependencies

**Add dependencies:**

    poetry add <package-name>

**Add development dependencies:**

    poetry add --dev <package-name>

**Remove a dependency:**

    poetry remove <package-name>

**Install all dependencies:**

    poetry install

## 4\. Configuring Repository & Authentication

    poetry config repositories.testpypi https://test.pypi.org/legacy/

    poetry config pypi-token.testpypi pypi-YOUR_API_TOKEN

    poetry config --list

## 5\. Building & Publishing a Package

    poetry build

    poetry publish -r testpypi

    poetry publish

    poetry publish -r testpypi -vvv

## 6\. Installing & Testing Published Package

    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple my_package

## 7\. Cleanup & Miscellaneous

    rm -rf dist/

</div>