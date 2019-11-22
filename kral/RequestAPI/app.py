import requests
import shutil

ipTong = "http://10.10.10.241:5000/"
ipTong2 = "http://10.10.10.241:5000/" #jina IP
ipAi = "http://10.10.10.128:5555/process"

r = requests.get(ipTong, stream=True)
if r.status_code == 200:
    with open("tong" + ".png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)

r = requests.get(ipTong2, stream=True)
if r.status_code == 200:
    with open("tong2" + ".png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)



'''r = requests.get(ipAi, stream=True)
if r.status_code == 200:
    with open("ai" + ".png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)

r = requests.get(ipAi, stream=True)'''

r = requests.post(ipAi, files={'img':open('tong.png', 'rb')})
if r.status_code == 200:
    response = int(r.content)
    print(response)

