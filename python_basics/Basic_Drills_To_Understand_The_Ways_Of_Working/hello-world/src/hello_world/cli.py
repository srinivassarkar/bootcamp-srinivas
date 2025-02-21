import typer
from .say_hello import say_hello

app = typer.Typer()

@app.command()
def hello(name: str):
    print(say_hello(name))

if __name__ == "__main__":
    app()