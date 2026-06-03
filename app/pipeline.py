# app/pipeline.py
from pathlib import Path
from app.services.conversion import convert_to_epub
from app.services.normalizer import normalize_epub
from app.services.metadata import update_epub_metadata

def process_file(path: str, kindle_mode: bool = False, title: str = None, author: str = None):
    original_path = Path(path)
    
    if not original_path.exists():
        print(f"❌ Erro: Arquivo de entrada não encontrado: {path}")
        return

    print(f"🚀 Iniciando processamento do arquivo: {original_path.name}")
    
    # Etapa 1: Conversão (Calibre Local)
    epub_path = convert_to_epub(original_path)
    
    if not epub_path:
        print("❌ Interrompendo pipeline: Falha na geração do EPUB intermediário.")
        return

    # Etapa 2: Normalização e Higienização de Código (HTML/CSS)
    if kindle_mode:
        epub_path = normalize_epub(epub_path)

    # Etapa 3: Injeção de Metadados Tratados
    if title or author:
        update_epub_metadata(epub_path, title=title, author=author)

    print(f"🎉 Pipeline concluído com sucesso!")
    print(f"📦 Arquivo pronto para o Kindle gerado em: {epub_path}")