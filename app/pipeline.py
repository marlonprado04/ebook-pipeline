# app/pipeline.py
from pathlib import Path
from app.services.conversion import convert_to_epub
from app.services.normalizer import normalize_epub

def process_file(path_str: str, kindle_mode: bool = False):
    original_path = Path(path_str)
    
    if not original_path.exists():
        print(f"❌ Erro: Arquivo não encontrado - {original_path}")
        return
        
    print(f"🚀 Iniciando processamento: {original_path.name}")
    
    # 1. Conversão
    epub_path = convert_to_epub(original_path)
    
    # 2. Normalização (Modo Kindle)
    if kindle_mode:
        epub_path = normalize_epub(epub_path)

    print(f"🎉 Processo finalizado! Arquivo pronto em: {epub_path}")