# app/cli.py
import typer
from app.pipeline import process_file

app = typer.Typer(no_args_is_help=True)

@app.command(name="convert")
def convert_command(
    path: str, 
    kindle: bool = typer.Option(False, "--kindle", help="Ativa a normalização estrutural para o Kindle"),
    title: str = typer.Option(None, "--title", "-t", help="Define um título customizado para o ebook"),
    author: str = typer.Option(None, "--author", "-a", help="Define o autor do ebook")
):
    """Processa e edita arquivos PDF/MOBI aplicando o pipeline completo do Calibre e normalizações."""
    process_file(path, kindle_mode=kindle, title=title, author=author)

if __name__ == "__main__":
    app()