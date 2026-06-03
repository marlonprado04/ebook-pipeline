# app/services/metadata.py
from pathlib import Path
from domain.models import EbookMetadata

def read_metadata(epub_path: Path) -> EbookMetadata:
    """Extrai os metadados atuais do EPUB."""
    # ToDo: Implementar parse do arquivo content.opf usando BeautifulSoup
    pass

def update_metadata(epub_path: Path, metadata: EbookMetadata) -> bool:
    """Sobrescreve os metadados do EPUB com as novas informações."""
    # ToDo: Atualizar content.opf e injetar nova imagem de capa
    pass