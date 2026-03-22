# app/cli.py
import typer
from app.pipeline import process_file

app = typer.Typer()

@app.command()
def convert(path: str, kindle: bool = False):
    process_file(path, kindle_mode=kindle)

if __name__ == "__main__":
    app()