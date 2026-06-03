# app/services/metadata.py
import zipfile
import os
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

def update_epub_metadata(epub_path: str, title: str = None, author: str = None) -> bool:
    """
    Abre o EPUB, localiza o arquivo de configuração (.opf) e atualiza
    o Título e o Autor do livro para garantir a exibição correta no Kindle.
    """
    path = Path(epub_path)
    if not path.exists():
        print(f"❌ Erro no Editor de Metadados: Arquivo não encontrado ({path})")
        return False

    # Se não foi passado metadado nenhum para alterar, pula o processo
    if not title and not author:
        return True

    print(f"🏷️ Atualizando metadados internos de: {path.name}...")
    
    temp_dir = path.parent / f"_temp_meta_{path.stem}"
    output_epub = path.parent / f"meta_updated_{path.name}"
    
    try:
        # 1. Extrai o EPUB
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # 2. Localiza o arquivo .opf (onde ficam guardados os metadados do livro)
        opf_file = next(temp_dir.rglob("*.opf"), None)
        
        if not opf_file:
            print("   [Aviso] Arquivo de metadados (.opf) não foi encontrado dentro do EPUB.")
            return False

        # 3. Lê e modifica o arquivo .opf usando BeautifulSoup (com parser XML para manter a estrutura)
        with open(opf_file, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo = f.read()

        soup = BeautifulSoup(conteudo, 'xml')

        # Atualiza o Título se foi fornecido
        if title:
            title_tag = soup.find('dc:title')
            if title_tag:
                title_tag.string = title
                print(f"   ↳ Título alterado para: '{title}'")

        # Atualiza o Autor se foi fornecido
        if author:
            author_tag = soup.find('dc:creator')
            if author_tag:
                author_tag.string = author
                print(f"   ↳ Autor alterado para: '{author}'")

        # Grava as alterações de volta no arquivo .opf
        with open(opf_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        # 4. Reconstrói o EPUB usando a lógica padrão (mimetype primeiro)
        reconstruir_epub(temp_dir, output_epub)
        
        # Substitui o arquivo antigo pelo novo com metadados atualizados
        path.unlink()
        output_epub.rename(path)
        
        print(f"✅ Metadados injetados com sucesso!")
        return True

    except Exception as e:
        print(f"⚠️ Falha ao atualizar metadados: {e}")
        return False
        
    finally:
        # Limpa os arquivos temporários
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

def reconstruir_epub(temp_dir: Path, output_zip_path: Path):
    """Compacta de volta seguindo estritamente a especificação EPUB."""
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        mimetype_path = temp_dir / 'mimetype'
        if mimetype_path.exists():
            zip_file.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)

        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = Path(root) / file
                archive_name = full_path.relative_to(temp_dir)
                if str(archive_name) == 'mimetype':
                    continue
                zip_file.write(full_path, archive_name)