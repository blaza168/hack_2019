import requests
import shutil

ipTong = "http://10.10.10.228:5000/"
ipTong2 = "http://10.10.10.241:5000/" #jina IP
ipAi = "http://10.10.10.128:5555/process"
tongLed = "http://10.10.10.155/0" #IP rasp 1
tongLed2 = "http://10.10.10.155/1" #IP rasp 2

while(True):
    r = requests.get(ipTong, stream=True)
    if r.status_code == 200:
        with open("tong" + ".jpg", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    r = requests.get(ipTong2, stream=True)
    if r.status_code == 200:
        with open("tong2" + ".jpg", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    tong1 = ''
    tong2 = ''

    r = requests.post(ipAi, files={'img':open('tong.jpg', 'rb')})
    if r.status_code == 200:
        response = int(r.content)
        tong1 = response

    r = requests.post(ipAi, files={'img':open('tong2.jpg', 'rb')})
    if r.status_code == 200:
        response = int(r.content)
        tong2 = response

    if tong1 > tong2:
        try:
            r = requests.get(tongLed, verify=False, timeout=1)
        except Exception:
            pass
    else:
        try:
            r = requests.get(tongLed2, verify=False, timeout=1)
        except Exception:
            pass



