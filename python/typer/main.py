import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """Say hello"""
    typer.echo(f"Hello {name}!")

@app.command()
def goodbye(name: str, formal: bool = False):
    """Say goodbye"""
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day!")
    else:
        typer.echo(f"Bye {name}!")

@app.command()
def launch():
    """Launch a website"""
    typer.launch(f"https://www.google.com")

def name_callback(name: str):
    if name != 'Bob':
        raise typer.BadParameter("Name should be Bob")
    return name + '_callback'

@app.command()
def callback(name: str = typer.Argument(..., callback=name_callback)):
    typer.echo(f"Hello {name}!")

@app.command()
def create(username: str):
    """Create a new user"""
    typer.echo(f"Creating user {username}")

@app.command()
def delete(username: str):
    """Delete a user"""
    typer.echo(f"Deleting user {username}")

@app.callback()
def main(ctx: typer.Context):
    typer.echo(f"About to execute command: {ctx.invoked_subcommand}")

if __name__ == "__main__":
    app()
