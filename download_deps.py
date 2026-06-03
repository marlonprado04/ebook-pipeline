import sys
import os
import urllib.request
import tarfile
import shutil
from pathlib import Path

# Links oficiais e estáveis
KCC_URL = "https://github.com/ciromattia/kcc/archive/refs/tags/v9.6.2.tar.gz"
CALIBRE_URL = "https://download.calibre-ebook.com/9.5.0/calibre-9.5.0-x86_64.txz"

def download_arquivo(url, destino):
    """Baixa um arquivo simulando um navegador legítimo."""
    print(f"📥 Baixando {url}...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(destino, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"✅ Download concluído: {destino}")
    except Exception as e:
        print(f"❌ Erro ao baixar o arquivo: {e}")
        if os.path.exists(destino):
            os.remove(destino)
        sys.exit(1)

def extrair_tar(arquivo_origem, pasta_destino):
    """Extrai arquivos .tar.gz ou .txz nativamente em qualquer SO."""
    Path(pasta_destino).mkdir(parents=True, exist_ok=True)
    print(f"📦 Extraindo {arquivo_origem}...")
    
    try:
        with tarfile.open(arquivo_origem, "r:*") as tar:
            if hasattr(tarfile, 'data_filter'):
                tar.extractall(path=pasta_destino, filter='data')
            else:
                tar.extractall(path=pasta_destino)
        print(f"✅ Extração concluída com sucesso.")
    except Exception as e:
        print(f"❌ Erro na extração do arquivo: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(arquivo_origem):
            os.remove(arquivo_origem)

def setup_kcc():
    print("\n🚀 Configurando KCC...")
    destino_kcc = Path("app/integrations/kcc/bin")
    
    if destino_kcc.exists():
        shutil.rmtree(destino_kcc)
    
    download_arquivo(KCC_URL, "kcc.tar.gz")
    
    pasta_pai = destino_kcc.parent
    extrair_tar("kcc.tar.gz", pasta_pai)
    
    pasta_extraida = pasta_pai / "kcc-9.6.2"
    if pasta_extraida.exists():
        pasta_extraida.rename(destino_kcc)
        print(f"✨ KCC organizado em: {destino_kcc}")
    else:
        print("⚠️ Atenção: Pasta extraída do KCC não encontrada no formato esperado.")

def setup_calibre():
    print(f"\n📚 Configurando Calibre ({sys.platform})...")
    destino_calibre = Path("app/integrations/calibre/bin")
    
    if destino_calibre.exists():
        shutil.rmtree(destino_calibre)
        
    download_arquivo(CALIBRE_URL, "calibre.txz")
    extrair_tar("calibre.txz", destino_calibre)
    print(f"✨ Calibre organizado em: {destino_calibre}")

def main():
    # Verifica se o SO é suportado antes de começar
    if not (sys.platform.startswith('linux') or sys.platform == 'win32'):
        print(f"❌ Sistema {sys.platform} não suportado.")
        sys.exit(1)

    setup_kcc()
    setup_calibre()
    
    print("\n🎉 Dependências instaladas e organizadas com sucesso!")

if __name__ == "__main__":
    main()