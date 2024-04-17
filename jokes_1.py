import requests
import json

limit = 3
api_url = f'https://api.api-ninjas.com/v1/jokes?limit={limit}'
response = requests.get(api_url, headers={'X-Api-Key': 'kyrasSHclrfdVD48zz5BeA==lsk0wGhxcE9eFbgy'})
if response.status_code == 200:
    content = response.json()
    joke = content[0]["joke"]
    print(joke)
else:
    print("Error:", response.status_code, response.text)