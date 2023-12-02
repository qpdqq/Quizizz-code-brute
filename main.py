import random
import requests
import json

print("""
.▄▄▄  ▄• ▄▌▪  ·▄▄▄▄•▪  ·▄▄▄▄•·▄▄▄▄•    ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .
▐▀•▀█ █▪██▌██ ▪▀·.█▌██ ▪▀·.█▌▪▀·.█▌    ▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·
█▌·.█▌█▌▐█▌▐█·▄█▀▀▀•▐█·▄█▀▀▀•▄█▀▀▀•    ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄
▐█▪▄█·▐█▄█▌▐█▌█▌▪▄█▀▐█▌█▌▪▄█▀█▌▪▄█▀    ██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌
·▀▀█.  ▀▀▀ ▀▀▀·▀▀▀ •▀▀▀·▀▀▀ •·▀▀▀ •    ·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ 
""")

while True:
    roomCode = random.randint(100000,999999)
    r = requests.post('https://game.quizizz.com/play-api/v5/checkRoom', data={"roomCode": str(roomCode)})
    if "room" in r.json() and "code" in r.json()["room"]:
        print("Success! Code: {}".format(r.json()["room"]["code"]))
        drt = input("Next?")
