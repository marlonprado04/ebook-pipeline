# 📚 Ebook Editor

## 🎯 Objetivo

Criar uma aplicação desktop simples para:

- Editar metadados de ebooks
- Converter múltiplos formatos para EPUB
- Padronizar estrutura de arquivos
- Garantir compatibilidade com Kindle
- Unificar fluxo hoje fragmentado entre Calibre, KCC e outras ferramentas similares

---

## 🧠 Problema

Ferramentas atuais possuem limitações:

### Calibre
- UI confusa e pesada
- Estrutura de pastas complexa
- Gera múltiplos formatos desnecessários
- EPUBs nem sempre compatíveis com Kindle moderno

### KCC (Kindle Comic Converter)
- Não permite edição de metadados
- Gera EPUBs “crus”

### Kindle
- Conversão interna inconsistente
- Sensível a EPUB mal estruturado

---

## 💡 Proposta

Criar um **pipeline unificado** com foco em:

> Simplicidade + Padronização + Compatibilidade

---

## 🧱 Arquitetura Geral

### Pipeline principal

```
INPUT
↓
[Detector de tipo]
↓
[Conversão]
  - Calibre (pdf, mobi)
  - KCC (cbz)
↓
[Normalização EPUB]
  - estrutura
  - CSS
  - imagens
↓
[Metadata Editor]
  - título, autor, série
  - capa
↓
[Polish opcional]
  - ebook-polish (Calibre)
↓
[Library Manager]
↓
OUTPUT (Kindle-ready)
```

### 📂 Estrutura o projeto

```
ebook-editor/
│
├── app/
│   ├── cli.py
│   ├── pipeline.py
│
├── services/
│   ├── conversion.py
│   ├── normalizer.py
│   ├── metadata.py
│   ├── library.py
│
├── integrations/
│   ├── calibre.py
│   ├── kcc.py
│
├── domain/
│   ├── models.py
│
├── utils/
│   ├── file_utils.py
│
├── tests/
│
└── pyproject.toml

```
---

## 📦 Escopo do MVP

### Funcionalidades

- D&D de arquivos ou seleção de pastas
- Suporte a:
  - `.epub`
  - `.mobi`
  - `.pdf`
  - `.cbz`
- Conversão automática para EPUB
- Editor de metadados:
  - título
  - autor
  - capa
  - idioma
  - serie
  - descrição
- Estrutura de saída padronizada
- Exportação única de arquivos
- Geração de EPUB compatível com Kindle

---

## 📂 Estrutura de arquivos

- Library 
  - Autor 
    - Serie (opcional)
      - Titulo - Volume x.epub
      - Capa.jpg

### Regras

- Apenas **1 formato final (EPUB)**
- Sem banco de dados obrigatório
- Sistema de arquivos = fonte da verdade

---

## 🔌 Integrações

### Conversão

- Calibre CLI (`ebook-convert`)
- Pandoc (opcional para PDF simples)

### Mangá

- KCC (Kindle Comic Converter)

### Manipulação EPUB

- ebooklib (Python)

---

## ⚙️ Componentes

### 1. Conversion Service
Responsável por:
- Detectar tipo de arquivo
- Chamar ferramentas externas
- Gerar EPUB intermediário

---

### 2. EPUB Normalizer

Responsável por:
- Limpar estrutura
- Garantir padrão EPUB 3
- Ajustar imagens
- Corrigir CSS
- Validar metadados mínimos

---

### 3. Metadata Editor

Responsável por:
- Ler metadados do EPUB
- Permitir edição
- Atualizar capa
- Persistir alterações

---

### 4. Library Manager

Responsável por:
- Organizar arquivos
- Aplicar padrão de nome
- Mover arquivos para estrutura final

---

### 5. UI (Desktop)

Responsável por:
- Upload (drag & drop) ou seleção de pastas
- Visualização de arquivos
- Edição de metadados
- Feedback do pipeline

---

## 🧠 Decisões Técnicas

### Backend
- Python

### Frontend
- Tauri (preferencial) ou Electron (ainda não definido)

### Comunicação
- API local

---

## 🚀 Fluxo do Usuário

1. Usuário arrasta arquivo ou seleciona multiplos arquivos de pasta
2. Sistema detecta tipo e lista os arquivos
3. Usuário clica para realizar conversão automática
4. Sistema abre lista de arquivos e editor de metadados
5. Usuário ajusta informações
6. Sistema normaliza EPUB
7. Arquivo é salvo na estrutura padrão

---

## ⭐ Diferencial Principal

### “Modo Kindle”

Botão único que:

- Normaliza EPUB
- Valida estrutura
- Garante compatibilidade
- Exporta arquivo pronto para envio


