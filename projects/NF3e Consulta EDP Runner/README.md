# nf3e-checksefaz-runner

Runner script to consult SEFAZ status for Brazilian NF-e / NF3-e documents using the Inventti API.  
Reads Excel files, extracts document keys, and performs automated API requests.

---

## 🇧🇷 Português

### 📌 Descrição
Script em Python para consultar documentos fiscais (NF-e / NF3-e) na SEFAZ via API da Inventti.

O script:
- Lê arquivos Excel (.xlsx)
- Busca a coluna **Chave**
- Executa requisições GET para cada documento
- Salva a resposta individualmente em arquivos JSON

Ideal para automação, auditoria fiscal e validação em massa.

---

### 📂 Estrutura esperada

```text
.
├── runner.py
├── Documento estornado - EDP ES.xlsx
├── Documento estornado - EDP SP.xlsx
└── responses/
    └── <chave>.json
```

---

### 📄 Formato do Excel
O arquivo deve conter uma coluna chamada:

```text
Chave
```

Cada linha deve conter uma chave de documento fiscal válida.

---

### ▶️ Como executar

```bash
pip install requests pandas openpyxl
python runner.py
```

---

### 📤 Saída
As respostas da API serão salvas em:

```text
responses/<chave>.json
```

---

## 🇺🇸 English

### 📌 Description
Python script to consult Brazilian fiscal documents (NF-e / NF3-e) in SEFAZ using the Inventti API.

The script:
- Reads Excel (.xlsx) files
- Extracts document keys from the **Chave** column
- Performs GET requests for each document
- Saves each response as an individual JSON file

Ideal for fiscal automation, auditing, and bulk validation.

---

### ▶️ How to run

```bash
pip install requests pandas openpyxl
python runner.py
```

---

### 📤 Output
API responses are saved in:

```text
responses/<document_key>.json
```

---

## 🇫🇷 Français

### 📌 Description
Script Python pour consulter les documents fiscaux brésiliens (NF-e / NF3-e) via la SEFAZ en utilisant l’API Inventti.

Le script :
- Lit des fichiers Excel (.xlsx)
- Extrait les clés fiscales depuis la colonne **Chave**
- Exécute des requêtes GET pour chaque document
- Sauvegarde chaque réponse dans un fichier JSON distinct

Idéal pour l’automatisation fiscale, l’audit et la validation en masse.

---

### ▶️ Exécution

```bash
pip install requests pandas openpyxl
python runner.py
```

---

### 📤 Sortie
Les réponses de l’API sont enregistrées dans :

```text
responses/<clé_du_document>.json
```

---

## ⚠️ Notes
- SSL certificate verification is disabled by default due to common Windows Python CA issues.
- Recommended for internal or controlled environments only.
- API rate limits may apply.

---

## 📄 License
MIT
