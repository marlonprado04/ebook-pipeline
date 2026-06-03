# app/services/conversion.py
from pathlib import Path
from app.domain.models import FileType
from app.integrations.calibre.adapter import convert_to_epub_via_calibre

def detect_file_type(path: Path) -> FileType:
    suffix = path.suffix.lower().replace(".", "")
    try:
        return FileType(suffix)
    except ValueError:
        return FileType.UNKNOWN

def convert_to_epub(file_path: str | Path) -> Path:
    path = Path(file_path)
    file_type = detect_file_type(path)
    
    if file_type == FileType.EPUB:
        print("ℹ️ Arquivo já é EPUB. Nenhuma conversão necessária.")
        return path
        
    if file_type == FileType.UNKNOWN:
        raise ValueError(f"❌ Formato não suportado para conversão: {path.suffix}")

    output_path = path.with_suffix('.epub')

    if file_type in [FileType.MOBI, FileType.PDF]:
        sucesso = convert_to_epub_via_calibre(path, output_path)
        if not sucesso:
            raise RuntimeError("Falha no pipeline de conversão do Calibre.")
            
    elif file_type == FileType.CBZ:
        print("🚧 [Aviso] A integração com o KCC será feita pelo módulo 'integrations/kcc/adapter.py' no futuro.")

    return output_path