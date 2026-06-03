# app/domain/models.py
from dataclasses import dataclass
from typing import Optional
from pathlib import Path
from enum import Enum

class FileType(Enum):
    EPUB = "epub"
    MOBI = "mobi"
    PDF = "pdf"
    CBZ = "cbz"
    UNKNOWN = "unknown"

@dataclass
class EbookMetadata:
    title: str
    author: str
    language: str = "pt-BR"
    series: Optional[str] = None
    volume: Optional[int] = None
    description: Optional[str] = None
    cover_path: Optional[Path] = None

@dataclass
class ConversionJob:
    original_path: Path
    file_type: FileType
    target_path: Optional[Path] = None
    metadata: Optional[EbookMetadata] = None
    is_kindle_ready: bool = False