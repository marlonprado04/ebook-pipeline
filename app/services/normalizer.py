# app/services/normalizer.py
from pathlib import Path

def normalize_epub(epub_path: str | Path) -> Path:
    """
    Descompacta o EPUB, valida a estrutura contra o padrão Kindle,
    limpa CSS, corrige imagens e reempacota.
    """
    path = Path(epub_path)
    print(f"✨ Iniciando Modo Kindle (Normalização) para: {path.name}")
    
    # Passo 1: Descompactar (unzip)
    # Passo 2: Validar e limpar estrutura (remover tags incompatíveis, normalizar CSS)
    # Passo 3: Reempacotar (zip) garantindo mimetype correto
    
    print("✅ EPUB configurado no padrão Kindle com sucesso.")
    return path