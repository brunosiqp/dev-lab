# NFCom Checksefaz API Runner

Simple Python script to execute API requests using a list of document IDs.

The script reads IDs from a `.txt` file and sends a request for each ID to the Inventti API.

---

# 🇧🇷 Português

## Descrição

Este script em Python lê um arquivo `ids.txt` contendo IDs de documentos fiscais e executa requisições para a API da Inventti.

Cada linha do arquivo deve conter um ID.

## Estrutura do Projeto

/project  
 ├── runner.py  
 └── ids.txt  

## Exemplo de ids.txt

14367983  
14367984  
14367985  

## Instalação

Instale a dependência necessária:

pip install requests

## Execução

python runner.py

O script irá executar uma requisição para cada ID listado no arquivo.

---

# 🇫🇷 Français

## Description

Ce script Python lit un fichier `ids.txt` contenant des identifiants de documents fiscaux et exécute des requêtes vers l'API Inventti.

Chaque ligne du fichier doit contenir un identifiant.

## Structure du projet

/project  
 ├── runner.py  
 └── ids.txt  

## Exemple de ids.txt

14367983  
14367984  
14367985  

## Installation

Installez la dépendance nécessaire :

pip install requests

## Exécution

python runner.py

Le script exécutera une requête pour chaque ID présent dans le fichier.

---

# 🇺🇸 English

## Description

This Python script reads a file called `ids.txt` containing fiscal document IDs and sends requests to the Inventti API.

Each line in the file must contain one ID.

## Project Structure

/project  
 ├── runner.py  
 └── ids.txt  

## Example ids.txt

14367983  
14367984  
14367985  

## Installation

Install the required dependency:

pip install requests

## Run

python runner.py

The script will execute one request for each ID listed in the file.