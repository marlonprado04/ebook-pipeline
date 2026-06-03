# app/pipeline.py
from pathlib import Path
from app.services.conversion import convert_to_epub
from app.services.normalizer import normalize_epub
from app.services.metadata import update_epub_metadata

def process_file(path: str, kindle_mode: bool = False, title: str = None, author: str = None):
    # 1. Converte (Calibre)
    epub_path = convert_to_epub(Path(path))
    
    # 2. Higieniza (Normalizador)
    if kindle_mode and epub_path:
        epub_path = normalize_epub(epub_path)
    
    # 3. Personaliza (Metadados)
    if (title or author) and epub_path:
        update_epub_metadata(epub_path, title=title, author=author)
        
    return str(epub_path) # Retorna o caminho final para a UI