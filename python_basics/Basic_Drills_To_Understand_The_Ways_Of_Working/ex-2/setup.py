from setuptools import setup, find_packages

setup(
    name="helloworld",
    version="0.1.0",
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=["typer"],  # Dependencies for your package
    entry_points={
        "console_scripts": [
            "hello=main:app",  # This assumes you have a main.py with a Typer app named 'app'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the Python version required
)