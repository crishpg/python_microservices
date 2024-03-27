
import requests
response = requests.post("http:///192.168.0.110:5000/api/user",
data={"key": "value"},
    headers={"Content-Type": "application/json"},
)
#response = requests.post("https://httpbin.org/post", 
    

print(response.json())
