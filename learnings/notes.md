<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poetry Cheat Sheet</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 20px; background-color: #f4f4f4; }
        h1, h2 { color: #333; }
        code { background-color: #eee; padding: 3px 6px; border-radius: 4px; }
        pre { background-color: #eee; padding: 10px; border-radius: 4px; overflow-x: auto; }
        .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
    </style>
</head>
<body>
    <div class="container">
        <h1>Poetry Cheat Sheet – From Project Setup to Publishing</h1>
        
        <h2>1. Install & Configure Poetry</h2>
        <pre><code>curl -sSL https://install.python-poetry.org | python3 -</code></pre>
        <p><strong>Verify installation:</strong></p>
        <pre><code>poetry --version</code></pre>
        
        <h2>2. Create & Set Up a New Project</h2>
        <pre><code>poetry new &lt;package-name&gt;</code></pre>
        <pre><code>cd &lt;package-name&gt;</code></pre>
        <pre><code>poetry init</code></pre>
        
        <h2>3. Managing Dependencies</h2>
        <p><strong>Add dependencies:</strong></p>
        <pre><code>poetry add &lt;package-name&gt;</code></pre>
        <p><strong>Add development dependencies:</strong></p>
        <pre><code>poetry add --dev &lt;package-name&gt;</code></pre>
        <p><strong>Remove a dependency:</strong></p>
        <pre><code>poetry remove &lt;package-name&gt;</code></pre>
        <p><strong>Install all dependencies:</strong></p>
        <pre><code>poetry install</code></pre>
        
        <h2>4. Configuring Repository & Authentication</h2>
        <pre><code>poetry config repositories.testpypi https://test.pypi.org/legacy/</code></pre>
        <pre><code>poetry config pypi-token.testpypi pypi-YOUR_API_TOKEN</code></pre>
        <pre><code>poetry config --list</code></pre>
        
        <h2>5. Building & Publishing a Package</h2>
        <pre><code>poetry build</code></pre>
        <pre><code>poetry publish -r testpypi</code></pre>
        <pre><code>poetry publish</code></pre>
        <pre><code>poetry publish -r testpypi -vvv</code></pre>
        
        <h2>6. Installing & Testing Published Package</h2>
        <pre><code>pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple my_package</code></pre>
        
        <h2>7. Cleanup & Miscellaneous</h2>
        <pre><code>rm -rf dist/</code></pre>
    </div>
</body>
</html>
