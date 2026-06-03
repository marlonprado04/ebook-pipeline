# app/services/normalizer.py
import zipfile
import os
import shutil
import re
from pathlib import Path
from bs4 import BeautifulSoup

def normalize_epub(epub_path: str) -> str:
    """
    Abre o EPUB, limpa estruturas de HTML/CSS internas, garante codificação 
    correta e otimiza o arquivo para leitura ideal no Kindle.
    """
    path = Path(epub_path)
    if not path.exists():
        print(f"❌ Erro no Normalizador: Arquivo não encontrado ({path})")
        return epub_path

    print(f"✨ Normalizando e limpando estrutura interna de: {path.name}...")
    
    # Criamos caminhos temporários para extração e reconstrução
    temp_dir = path.parent / f"_temp_{path.stem}"
    output_epub = path.parent / f"normalized_{path.name}"
    
    try:
        # 1. Extrai o EPUB (que é um arquivo ZIP protegido)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # 2. Varre os arquivos extraídos procurando conteúdos HTML/XHTML/CSS
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = Path(root) / file
                
                # Tratar arquivos de texto/HTML internos do livro
                if file.endswith(('.html', '.xhtml', '.htm')):
                    limpar_e_corrigir_html(file_path)
                
                # Tratar estilizações (CSS)
                elif file.endswith('.css'):
                    otimizar_css(file_path)

        # 3. Reconstrói o EPUB mantendo a especificação original (mimetype precisa ser o primeiro)
        reconstruir_epub(temp_dir, output_epub)
        
        # 4. Substitui o arquivo original pelo corrigido/limpo
        path.unlink()  # Deleta o antigo intermediário do Calibre
        output_epub.rename(path)  # Renomeia o novo limpo para o nome original
        
        print(f"✅ EPUB normalizado com sucesso!")
        return str(path)

    except Exception as e:
        print(f"⚠️ Falha ao normalizar EPUB: {e}. Mantendo versão original.")
        return epub_path
        
    finally:
        # Limpa a sujeira/pasta temporária
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

def limpar_e_corrigir_html(file_path: Path):
    """Abre o arquivo de texto do livro, limpa tags inúteis e garante UTF-8."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo = f.read()

        soup = BeautifulSoup(conteudo, 'html.parser')

        # 🧹 Remover tags de scripts e sujeiras comuns que travam o Kindle
        for tag in soup.find_all(['script', 'style', 'iframe']):
            tag.decompose()

        # Garante que o cabeçalho declara a codificação correta
        meta_html = soup.find('meta', charset=True)
        if not meta_html:
            meta_tag = soup.new_tag('meta', charset='utf-8')
            if soup.head:
                soup.head.append(meta_tag)

        # Reescreve o arquivo higienizado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
    except Exception as e:
        print(f"   [Aviso] Falha ao processar HTML {file_path.name}: {e}")

def otimizar_css(file_path: Path):
    """Remove propriedades CSS problemáticas que estragam a formatação no Kindle."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            css_conteudo = f.read()

        # Remove margens absolutas pesadas que matam o redimensionamento do Kindle
        css_limpo = re.sub(r'margin:\s*[^;]+;[^\n]*', '', css_conteudo)
        # Força fontes a serem dinâmicas (evita travar uma fonte fixa que o usuário não consiga mudar)
        css_limpo = re.sub(r'font-family:\s*[^;]+;', '', css_limpo)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(css_limpo)
    except Exception as e:
        print(f"   [Aviso] Falha ao processar CSS {file_path.name}: {e}")

def reconstruir_epub(temp_dir: Path, output_zip_path: Path):
    """Compacta de volta os arquivos seguindo estritamente a regra do formato EPUB."""
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # O arquivo 'mimetype' DEVE ser o primeiro e NÃO pode ser compactado (Stored)
        mimetype_path = temp_dir / 'mimetype'
        if mimetype_path.exists():
            zip_file.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)

        # Adiciona o restante das pastas e arquivos de forma normal
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = Path(root) / file
                archive_name = full_path.relative_to(temp_dir)
                
                # Pula o mimetype que já foi adicionado
                if str(archive_name) == 'mimetype':
                    continue
                    
                zip_file.write(full_path, archive_name)