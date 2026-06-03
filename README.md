# 📚 Ebook Pipeline

## 🎯 Objetivo
Ferramenta desktop leve para automação de conversão, normalização e higienização de ebooks (EPUB, MOBI, PDF), focada em máxima compatibilidade com leitores Kindle e organização profissional.

## 🚀 O que já foi implementado (MVP)
- Motor de Conversão: Integração nativa com ebook-convert (Calibre) para conversão de formatos brutos.
- Normalizador de Ebooks: Limpeza de tags HTML, remoção de CSS com margens fixas e otimização de estrutura interna.
- Editor de Metadados: Injeção direta de Título, Autor e Capa via manipulação de arquivos .opf.
- Interface Gráfica (GUI): Interface moderna e responsiva feita com HTML/CSS, integrada via Eel (Python-to-Web).

## 🧱 Arquitetura e Estrutura
O projeto opera com uma separação clara entre a lógica de negócio (app/) e a interface (ui/):

ebook-pipeline/
├── app/                  # Core do Pipeline
│   ├── integrations/     # Adaptadores (Calibre, KCC)
│   ├── services/         # Normalização, Metadados, Conversão
│   ├── domain/           # Modelos de dados
│   └── pipeline.py       # Orquestrador Central
├── ui/                   # Interface Gráfica
│   ├── index.html        # Estrutura
│   ├── style.css         # Design Pattern
│   └── app.js            # Lógica de conexão com Python
├── main.py               # Ponto de entrada (Servidor Eel)
└── setup.py              # Instalação como pacote local

## ⚙️ Como rodar o projeto

### Pré-requisitos
- Python 3.10+ instalado.
- Calibre: O projeto possui um script para baixar e configurar uma versão portátil automaticamente. Não é necessário instalar o Calibre manualmente pelo site oficial.

### Instalação
1. Clone o repositório.
2. No diretório raiz, instale as dependências e o pacote em modo editável:
   `pip install -r requirements.txt`
   `pip install -e .`
3. Execute o script de dependências para baixar o motor do Calibre internamente:
   `python download_deps.py`

### Execução
Para abrir a interface gráfica:
   `python main.py`

## 🔌 Integrações e Fluxo
* Pipeline Linear: O arquivo entra, é convertido pelo Calibre, passa pelo Normalizador (BeautifulSoup4) que limpa o lixo de HTML e CSS, e finalmente recebe os Metadados injetados.
* Modo Kindle: Ao ativar, o sistema aplica automaticamente a limpeza de margens absolutas e fontes, garantindo que o seu Kindle consiga redimensionar o texto perfeitamente.
* Comunicação: O frontend (app.js) invoca funções Python diretamente via @eel.expose no main.py.

## 🛠️ Próximos Passos
* [ ] Integração KCC: Implementar o adapter para processamento de CBZ/Quadrinhos.
* [ ] Polimento UX: Adicionar indicadores de carregamento (spinner) na UI durante o processamento.
* [ ] Empacotamento: Criar script .bat ou executável (pyinstaller) para distribuição.
* [ ] Gestão de Capas: Finalizar a injeção via injetar_capa no metadata.py.

Desenvolvido com foco em: Simplicidade, Padronização e Compatibilidade.