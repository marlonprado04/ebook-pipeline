# download_deps.py
import os
import sys
import urllib.request
import subprocess
from pathlib import Path

# Configura as pastas de destino
BASE_DIR = Path(__file__).parent.resolve()
CALIBRE_BIN_DIR = BASE_DIR / "app" / "integrations" / "calibre" / "bin"
KCC_BIN_DIR = BASE_DIR / "app" / "integrations" / "kcc" / "bin"

def criar_pastas():
    CALIBRE_BIN_DIR.mkdir(parents=True, exist_ok=True)
    KCC_BIN_DIR.mkdir(parents=True, exist_ok=True)

def baixar_arquivo(url, destino):
    print(f"📦 Baixando {url}...")
    urllib.request.urlretrieve(url, destino)
    print("✅ Download concluído!")

def configurar_calibre_windows():
    # Usaremos uma versão estável do Calibre de 64 bits para Windows (.msi)
    url_calibre = "https://download.calibre-ebook.com/7.25.0/calibre-64bit-7.25.0.msi"
    msi_path = BASE_DIR / "calibre_installer.msi"
    
    baixar_arquivo(url_calibre, msi_path)
    
    print(f"📂 Extraindo arquivos do Calibre para {CALIBRE_BIN_DIR}...")
    # O Windows possui o 'msiexec' nativo, que permite extrair o instalador sem instalar no sistema
    comando = [
        "msiexec",
        "/a", str(msi_path),         # Modo administrativo (apenas extrai os arquivos)
        "/qb",                       # Interface básica/silenciosa
        f"TARGETDIR={CALIBRE_BIN_DIR}" # Pasta de destino interna do projeto
    ]
    
    try:
        subprocess.run(comando, check=True)
        print("✅ Calibre extraído com sucesso dentro do projeto!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao extrair o Calibre: {e}")
    finally:
        # Limpa o instalador pesado que foi baixado
        if msi_path.exists():
            os.remove(msi_path)

def main():
    if sys.platform != "win32":
        print("❌ Este script foi adaptado especificamente para o seu ambiente Windows nativo.")
        return

    print("🚀 Iniciando o download das dependências do projeto...")
    criar_pastas()
    configurar_calibre_windows()
    print("\n🎉 Tudo pronto! Dependências configuradas para o ambiente Windows.")

if __name__ == "__main__":
    main()