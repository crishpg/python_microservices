import requests
import json
from faker import Faker
faker = Faker()

""" nome = "name:" + (faker.name())
endereco = "email:" + ( faker.email())
string = {
  nome,
  endereco
}
print (string)
 """




url = "http://54.167.13.147:5000/api/user"

payload = json.dumps({
  "name": 'Cristiano Schmitt',
  "email": "Luis@gmail.com"
}) 

headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
