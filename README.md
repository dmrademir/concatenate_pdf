# 📄 PDF Merger with A4 Normalization

Script em Python para **mesclar múltiplos PDFs** em um único arquivo, garantindo que **todas as páginas sejam padronizadas no formato A4**. Também adiciona automaticamente uma **página de capa** após cada documento.

---

## 🚀 Funcionalidades

* 🔗 Mescla vários PDFs em sequência
* 📐 Normaliza todas as páginas para tamanho A4
* 📑 Insere uma capa padrão após cada documento
* ⚠️ Trata erros básicos (pastas inexistentes, ausência de arquivos)

---

## 📁 Estrutura de Pastas

```
project/
│
├── concatenate_pdf.py
├── documents/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
│
├── covers/
│   └── standard_cover.pdf
│
└── merged_document.pdf (gerado automaticamente)
```

---

## ⚙️ Pré-requisitos

* Python 3.8+
* Biblioteca:

```bash
pip install pypdf
```

---

## ▶️ Como usar

1. **Adicione os PDFs**

   * Coloque os arquivos que deseja mesclar dentro da pasta:

     ```
     ./documents
     ```

2. **Adicione a capa (opcional, mas recomendado)**

   * Coloque o arquivo:

     ```
     ./covers/standard_cover.pdf
     ```

3. **Execute o script**

```
    python concatenate_pdf.py
    
```

4. **Resultado**

   * O arquivo final será gerado como:

     ```
     merged_document.pdf
     ```

---

## 🔄 Lógica de Processamento

Para cada arquivo em `documents/`, o script:

1. Lê o PDF
2. Redimensiona todas as páginas para A4
3. Adiciona as páginas ao arquivo final
4. Procura por `standard_cover.pdf`
5. Se existir:

   * Redimensiona e adiciona a capa após o documento
6. Repete o processo para o próximo arquivo

---

## ⚠️ Tratamento de Erros

* Pasta `documents` inexistente → erro e interrupção
* Nenhum PDF encontrado → aviso e interrupção
* Capa não encontrada → aviso, mas continua execução
* Erro ao salvar → mensagem de erro exibida

---

## 🧠 Observações Técnicas

* A ordenação dos arquivos é feita alfabeticamente (`sorted`)
* A normalização usa:

  ```python
  page.scale_to(width=A4_WIDTH, height=A4_HEIGHT)
  ```
* Dimensões A4 são obtidas via:

  ```python
  PaperSize.A4
  ```


