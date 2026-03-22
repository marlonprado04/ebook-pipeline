# app/pipeline.py
from services.conversion import convert_to_epub
from services.normalizer import normalize_epub

def process_file(path: str, kindle_mode: bool = False):
    epub_path = convert_to_epub(path)
    
    if kindle_mode:
        epub_path = normalize_epub(epub_path)

    print(f"Arquivo gerado: {epub_path}")