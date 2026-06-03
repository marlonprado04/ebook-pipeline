# app/pipeline.py
from pathlib import Path
from app.services.conversion import convert_to_epub
from app.services.normalizer import normalize_epub

def process_file(path: str, kindle_mode: bool = False):
    original_path = Path(path)
    
    if not original_path.exists():
        print(f"❌ Erro: Arquivo de entrada não encontrado: {path}")
        return

    print(f"🚀 Iniciando processamento: {original_path.name}")
    
    # 1. Conversão Inicial (Chama o Calibre Local que configuramos)
    epub_path = convert_to_epub(original_path)
    
    # 2. Normalização (Modo Kindle Ativado)
    if kindle_mode and epub_path:
        epub_path = normalize_epub(epub_path)

    print(f"🎉 Processo concluído! Arquivo gerado em: {epub_path}")