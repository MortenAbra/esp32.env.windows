import requests

payload = '123456789,12,23,1'
url = 'http://127.0.0.1:8000/store/local'

for i in range(1,100):
    requests.post(url, payload)