# app/integrations/calibre/adapter.py
import subprocess
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()

def get_calibre_executable() -> Path:
    """Retorna o caminho para o executável do Calibre embutido no projeto."""
    bin_dir = CURRENT_DIR / "bin"
    
    if sys.platform == "win32":
        # Faz uma busca recursiva (rglob) por 'ebook-convert.exe' dentro da pasta bin
        executavel_encontrado = next(bin_dir.rglob("ebook-convert.exe"), None)
        
        if executavel_encontrado:
            return executavel_encontrado
            
        # Fallback caso não encontre nada na busca dinâmica
        return bin_dir / "PFiles" / "Calibre" / "ebook-convert.exe"
    else:
        return bin_dir / "ebook-convert"

def convert_to_epub_via_calibre(input_path: Path, output_path: Path) -> bool:
    executable_path = get_calibre_executable()
    
    if not executable_path.exists():
        print(f"❌ Erro FATAL: Executável do Calibre não encontrado na pasta local 'bin'.")
        print("💡 Certifique-se de que rodou o script 'python download_deps.py' até o final.")
        return False

    if not input_path.exists():
        print(f"❌ Erro: O arquivo de entrada não existe ({input_path})")
        return False

    command = [
        str(executable_path),
        str(input_path),
        str(output_path)
    ]
    
    print(f"🔄 Acionando Calibre local encontrado em: {executable_path.relative_to(CURRENT_DIR.parent.parent.parent)}")
    print(f"🔄 Convertendo: {input_path.name}...")
    
    try:
        # Captura saída para debug caso precise
        subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"✅ Conversão concluída com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro durante a conversão no Calibre:")
        print(e.stderr if e.stderr else e.stdout)
        return False