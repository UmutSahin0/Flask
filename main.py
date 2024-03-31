import requests

x = requests.get('http://localhost:5000/id/1')
print(x.text)