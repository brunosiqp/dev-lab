import requests

API_KEY = 44d3e21f4a3341c7bdd6272847a52ee9
BASE_URL = httpssaas.inventti.appnfcomapiv1documentosfiscais

headers = {
    x-api-key API_KEY
}

with open(ids.txt, r) as file
    ids = [line.strip() for line in file if line.strip()]

for doc_id in ids
    url = f{BASE_URL}{doc_id}
    
    try
        response = requests.get(url, headers=headers)
        
        print(fID {doc_id}  Status {response.status_code})
        
        if response.status_code == 200
            print(response.json())
        else
            print(response.text)

    except Exception as e
        print(fErro no ID {doc_id} {e})