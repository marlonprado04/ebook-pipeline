# Anotações durante desenvolvimento (Dev Journal)

## Comandos Calibre:

### Referencias:

**Link do site oficial Calibre:** `https://calibre-ebook.com/download_linux`


**Download dos binários:** `wget https://download.calibre-ebook.com/9.5.0/calibre-9.5.0-x86_64.txz`

**Comando para descompactar binario:** `tar -xvf  calibre-9.5.0-x86_64.txz -C calibre/`

### Documentação

**Ebook-convert:**

  - ebook-convert input_file output_file [options] 
  
**Options:**

  - epub-version: versão do epub utilizada. Pode ser 2 ou 3, para melhor compatibilidade
  - no-default-epub-cover: remove a capa padrão que vai aom o nome do titulo, autor, etc
  - no-svg-cover: não usar capa em SVG, deve ser usado para programas que não suportam capa SVG

## Comandos KCC:

**Link de download:** `wget https://github.com/ciromattia/kcc/archive/refs/tags/v9.6.2.tar.gz`

**Comando para descompactar binario:** `tar -xvf v9.6.2.tar.gz -C kcc/`

### Documentação 

**Instalação de dependencias necessarias:**

`sudo apt-get install python3 p7zip-full python3-pil python3-psutil python3-slugify`

