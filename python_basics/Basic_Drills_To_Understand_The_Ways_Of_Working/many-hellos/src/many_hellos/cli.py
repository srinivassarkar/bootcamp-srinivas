

# import typer
# import logging
# from hello_world.say_hello import say_hello

# app = typer.Typer()

# @app.command()
# def hello(names: list[str]):
#     logging.basicConfig(level=logging.INFO)
#     for name in names:
#         print(say_hello(name))

# if __name__ == "__main__":
#     app()


# many_hellos/cli.py

# import typer
# import logging
# from hello_world.say_hello import say_hello

# app = typer.Typer()

# @app.command()
# def hello(names: list[str]):
#     logging.basicConfig(level=logging.WARNING)
#     for name in names:
#         print(say_hello(name))

# if __name__ == "__main__":
#     app()


# many_hellos/cli.py

import typer
import logging
from hello_world.say_hello import say_hello

app = typer.Typer()

@app.command()
def hello(names: list[str]):
    logging.basicConfig(level=logging.WARNING)
    logging.getLogger("hello_world.config").setLevel(logging.INFO)
    for name in names:
        print(say_hello(name))

if __name__ == "__main__":
    app()