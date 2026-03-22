# 📄 ADR - Architectural Decision Record

## ADR-001: Uso de ferramentas externas para conversão

### Status
Aceito

### Contexto

Conversão de formatos como PDF, MOBI e CBZ para EPUB é complexa e já resolvida parcialmente por ferramentas existentes.

### Decisão

Utilizar ferramentas externas:

- Calibre CLI para conversão geral
- KCC para mangás

### Consequências

#### Positivas
- Redução drástica de complexidade
- Aproveitamento de soluções maduras
- MVP mais rápido

#### Negativas
- Dependência externa
- Necessidade de lidar com erros dessas ferramentas

---

## ADR-002: EPUB como formato único

### Status
Aceito

### Contexto

Calibre trabalha com múltiplos formatos por livro, gerando complexidade desnecessária.

### Decisão

Padronizar saída para:

> Apenas EPUB

### Consequências

#### Positivas
- Simplicidade
- Menor uso de armazenamento
- Melhor controle de qualidade

#### Negativas
- Perda de flexibilidade para outros formatos

---

## ADR-003: File System como fonte da verdade

### Status
Aceito

### Contexto

Calibre depende de banco interno, dificultando interoperabilidade.

### Decisão

Não usar banco de dados obrigatório.
Organização baseada em pastas do sistema e arquivos.

### Consequências

#### Positivas
- Transparência
- Fácil backup
- Independência da aplicação

#### Negativas
- Menor capacidade de queries complexas

---

## ADR-004: Pipeline obrigatório

### Status
Aceito

### Contexto

Ferramentas atuais não garantem consistência entre etapas.

### Decisão

Todo arquivo deve passar por:

> Conversão → Normalização → Metadados → Organização


### Consequências

#### Positivas
- Consistência
- Qualidade previsível
- Melhor compatibilidade com Kindle

#### Negativas
- Processamento adicional

---

## ADR-005: Não reinventar conversão

### Status
Aceito

### Contexto

Conversão de ebooks é tecnicamente complexa e fora do escopo do MVP.

### Decisão

Não implementar conversores próprios.

### Consequências

#### Positivas
- Foco no diferencial (UX + pipeline)
- Redução de risco

#### Negativas
- Menor controle sobre conversão