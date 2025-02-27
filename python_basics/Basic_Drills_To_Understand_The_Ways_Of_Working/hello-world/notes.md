<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>say_helloo - Python Package</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
        }
        code {
            background: #ecf0f1;
            padding: 5px;
            border-radius: 5px;
            display: block;
            white-space: pre-wrap;
        }
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: #7f8c8d;
            text-align: center;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>say_helloo - Python Package</h1>
        <p><strong>Overview:</strong> A simple Python package to print "Hello, World!".</p>

        <h2>Project Structure</h2>
        <code>
hello-world/
│── hello_world/
│   ├── __init__.py
│   ├── say_hello.py   # Contains say_hello() function
│── tests/             # Unit tests
│── pyproject.toml     # Poetry config
│── README.md
        </code>

        <h2>Installation & Usage</h2>
        <h3>1. Install from TestPyPI</h3>
        <code>pip install -i https://test.pypi.org/simple/ say_helloo</code>

        <h3>2. Import & Use</h3>
        <code>
from hello_world.say_hello import say_hello
say_hello()
        </code>

        <h2>Development Approach</h2>
        <ol>
            <li>Create a package (<code>hello_world/</code>) with <code>say_hello.py</code>.</li>
            <li>Manage dependencies with Poetry (<code>pyproject.toml</code>).</li>
            <li>Write tests in the <code>tests/</code> folder.</li>
            <li>Build the package using Poetry:</li>
        </ol>
        <code>poetry build</code>

        <h2>Run Commands</h2>
        <ul>
            <li><strong>Install Poetry:</strong> <code>pip install poetry</code></li>
            <li><strong>Create Virtual Env:</strong> <code>poetry shell</code></li>
            <li><strong>Install Dependencies:</strong> <code>poetry install</code></li>
            <li><strong>Run Tests:</strong> <code>poetry run pytest</code></li>
            <li><strong>Build Package:</strong> <code>poetry build</code></li>
            <li><strong>Publish to PyPI:</strong> <code>poetry publish -r testpypi</code></li>
        </ul>

        <div class="footer">
            Created by ChatGPT
        </div>
    </div>

</body>
</html>
