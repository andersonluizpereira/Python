import requests
from datetime import datetime
from flask import Flask
import hashlib

config = {
         "apikey": "f2aef569ee6f38276c60b9264d1dec2b",
         "privatekey": "0126a49f00e1063a8f441de67dfd56090cb24be6",
         "limit":'10',
         "urlbase":"https://gateway.marvel.com/v1/public/comics"
         }

def convert_ticks():
    t0 = datetime(1, 1, 1)
    now = datetime.utcnow()
    seconds = (now - t0).total_seconds()
    return int(seconds * 10**7)


def generatadmd5():
    key = str(convert_ticks()) +config.get('privatekey') +config.get('apikey')
    return hashlib.md5(key .encode()).hexdigest()


url=''+config.get('urlbase')+'?ts='+str(convert_ticks())+'&apikey='+config.get('apikey')+'&hash='+generatadmd5()+'&limit='+config.get('limit')+''

res = requests.get(url)