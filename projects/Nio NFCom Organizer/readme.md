# SQL Generator from Excel / Nio NFCom Organizer

Python script that reads an Excel file and generates a SQL query for selecting fiscal documents.

The script extracts values from the spreadsheet and builds a VALUES block used in a SQL JOIN.

---

# 🇧🇷 Português

## Descrição

Este script lê um arquivo Excel (.xlsx) contendo dados de documentos fiscais e gera automaticamente uma query SQL no formato:

SELECT df.*
FROM documento_fiscal df
JOIN (VALUES ...) v(...)

Os dados são extraídos das seguintes colunas da planilha:

CNPJ EMISSOR → empresa_cnpj  
NUM_NF → nnf  
SÉRIE → serie  

O CNPJ é automaticamente normalizado para conter apenas números.

Exemplo:

53.420.564/0011-11 → 53420564001111

## Estrutura do Projeto

/project  
 ├── gerar_select.py  
 └── dados.xlsx  

## Instalação

pip install pandas openpyxl

## Execução

python gerar_select.py

O script irá gerar um arquivo chamado:

select.sql

contendo a query SQL completa.

---

# 🇫🇷 Français

## Description

Ce script Python lit un fichier Excel (.xlsx) contenant des informations de documents fiscaux et génère automatiquement une requête SQL.

Les données sont extraites des colonnes suivantes :

CNPJ EMISSOR → empresa_cnpj  
NUM_NF → nnf  
SÉRIE → serie  

Le CNPJ est automatiquement nettoyé pour ne conserver que les chiffres.

Exemple :

53.420.564/0011-11 → 53420564001111

## Structure du projet

/project  
 ├── gerar_select.py  
 └── dados.xlsx  

## Installation

pip install pandas openpyxl

## Exécution

python gerar_select.py

Un fichier select.sql sera généré avec la requête SQL complète.

---

# 🇺🇸 English

## Description

This Python script reads an Excel file (.xlsx) containing fiscal document data and automatically generates a SQL query.

The script extracts values from the following columns:

CNPJ EMISSOR → empresa_cnpj  
NUM_NF → nnf  
SÉRIE → serie  

The CNPJ value is automatically cleaned to contain only numeric characters.

Example:

53.420.564/0011-11 → 53420564001111

## Project Structure

/project  
 ├── gerar_select.py  
 └── dados.xlsx  

## Installation

pip install pandas openpyxl

## Run

python gerar_select.py

The script will generate a file called:

select.sql

containing the full SQL query.