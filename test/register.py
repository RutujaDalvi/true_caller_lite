#make a POST request
import requests
dictToSend = {'name': 'Sunny', 'phoneNumber': '9503284884', 'password': 'SunnyUnde'}
res = requests.post('http://localhost:5000/register', json=dictToSend)
print('response from server:',res.text)
dictFromServer = res.json()