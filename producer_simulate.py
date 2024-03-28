import requests
import json
from faker import Faker
faker = Faker()
from jsf import JSF

faker = JSF(
    {
        "type": "object",
        "properties": {
            "name": {"type": "string", "$provider": "faker.name"},
            "email": {"type": "string", "$provider": "faker.email"},
        },
        "required": ["name", "email"],
    }
)

fake_json = faker.generate()
#print(json.dumps(fake_json, sort_keys=True, indent=4))
#print (fake_json)


url = "http://localhost:5000/api/user"

payload = json.dumps(
fake_json, sort_keys=True, indent=4) 
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
