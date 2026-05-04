# 📄 Architecture Project PDF Merger

Python script to merge multiple technical PDFs into a single document, with optional section covers.

Each document is processed with:

* Optional **specific cover per document**
* Optional **default fallback cover**
* Pages resized to **A4 while preserving aspect ratio**
* Content automatically centered on the page

---

## 📁 Folder Structure

Organize your project as follows:

```bash
project/
│
├── concatenate_pdf.py
├── documents/
│   ├── electrical.pdf
│   ├── hydraulic.pdf
│   └── ...
│
├── covers/
│   ├── electrical.pdf
│   ├── hydraulic.pdf
│   └── default.pdf
```

### Rules

* All input PDFs must be placed inside `documents/`
* Covers are optional and must be placed inside `covers/`

Cover selection follows this order:

1. A cover with the **same name as the document**

   * `documents/electrical.pdf` → `covers/electrical.pdf`
2. If not found, uses:

   * `covers/default.pdf`
3. If neither exists:

   * No cover is added

---

## 📦 Requirements

Install the required dependency:

```bash
pip install pypdf
```

---

## ▶️ Usage

1. Add your PDF files to:

```bash
./documents
```

2. (Optional) Add cover files to:

```bash
./covers
```

3. Run the script:

```bash
python concatenate_pdf.py
```

---

## 📄 Output

The generated file will be:

```bash
project_complete.pdf
```

---

## 🔄 Output Structure

Example input:

```bash
documents/
  electrical.pdf
  hydraulic.pdf

covers/
  electrical.pdf
  default.pdf
```

Result:

```
[COVER: electrical.pdf]
[electrical.pdf pages]

[COVER: default.pdf]
[hydraulic.pdf pages]
```

---

## 📌 Notes for Usage

* File order is alphabetical by default
* To control order, prefix file names:

```bash
01_electrical.pdf
02_hydraulic.pdf
03_structural.pdf
```

* Covers must match file names exactly (including extension)

---

If needed, this setup can be extended to support CLI arguments or external configuration files.