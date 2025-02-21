import typer
from helloworld.sayhello import say_hello

app = typer.Typer()

@app.command()
def hello(name: str):
    result = say_hello(name)
    typer.echo(result)

if __name__ == "__main__":
    app()