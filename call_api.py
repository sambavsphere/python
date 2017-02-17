import requests

resp = requests.get('http://host:port/users')
pritn resp.json()
resp = request.post("http://host:port/users", json={key:value})
print resp
