# main.py
import sys
import os
import io

# Adiciona o diretório atual ao caminho do sistema, garantindo que o Python ache a pasta 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import eel
from app.pipeline import process_file

# Redireciona stdout para aceitar caracteres UTF-8 ignorando erros de codificação do terminal Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

eel.init('ui')

@eel.expose
def processar_livro_gui(path, kindle, title, author):
    """Função que o JavaScript chama para disparar o pipeline."""
    try:
        # Chama a função que já criamos e funciona
        caminho_final = process_file(path, kindle_mode=kindle, title=title, author=author)
        return {"status": "success", "message": f"Concluído: {caminho_final}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Inicia o app (abre o navegador no index.html)
if __name__ == '__main__':
    eel.start('index.html', size=(700, 650))