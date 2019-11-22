import requests
import shutil

import time

ipTong = "http://10.10.10.241:5000/"
ipAi = "<nejaka ip>"

r = requests.get(ipTong, stream=True)
if r.status_code == 200:
    with open("tong" + ".png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)

'''r = requests.get(ipAi, stream=True)
if r.status_code == 200:
    with open("ai" + ".png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)

r = requests.get(ipAi, stream=True)'''