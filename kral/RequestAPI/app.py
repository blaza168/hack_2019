import requests
import shutil

ipTong = "http://10.10.9.51:5000/"
ipTong2 = "http://10.10.9.50:5000/" #jina IP
ipAi = "http://10.10.9.52:5555/process"
tongLed = "http://10.10.9.53/0" #IP rasp 1
tongLed2 = "http://10.10.9.53/1" #IP rasp 2

tong1_less = None

while(True):
    r = requests.get(ipTong, stream=True)
    if r.status_code == 200:
        with open("tong" + ".jpg", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    r = requests.get(ipTong2, stream=True)
    if r.status_code == 200:
        with open("tong2" + ".jpg", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    tong1 = 0
    tong2 = 0

    r = requests.post(ipAi, files={'img':open('tong.jpg', 'rb')})
    if r.status_code == 200:
        response = int(r.content)
        tong1 = response

    r = requests.post(ipAi, files={'img':open('tong2.jpg', 'rb')})
    if r.status_code == 200:
        response = int(r.content)
        tong2 = response

    print("Counts: C1: {}, C2 {}".format(tong1, tong2))

    if tong1 > tong2:
        try:
            if tong1_less != False:
                print("Sending request to /1")
                tong1_less = False
                r = requests.get(tongLed, verify=False, timeout=1)
            else:
                print("Not sending request: {}".format(tong1_less))
        except Exception:
            print("Catched exception")
            pass
    if tong2 > tong1:
        try:
            if tong1_less != True:
                print("Sending request to /0")
                tong1_less = True
                r = requests.get(tongLed2, verify=False, timeout=1)
            else:
                print("Not sending request: {}".format(tong1_less))
        except Exception:
            print("Catched exception")
            pass



