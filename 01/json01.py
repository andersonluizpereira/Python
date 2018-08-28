import requests
from datetime import datetime
from flask import Flask
import hashlib

config = {
         "apikey": "f2aef569ee6f38276c60b9264d1dec2b",
         "privatekey": "0126a49f00e1063a8f441de67dfd56090cb24be6",
         "limit":'10',
         "urlbase":"https://gateway.marvel.com/v1/public"
         }

def convert_ticks():
    t0 = datetime(1, 1, 1)
    now = datetime.utcnow()
    seconds = (now - t0).total_seconds()
    return int(seconds * 10**7)


def generatadmd5():
    key = str(convert_ticks()) +config.get('privatekey') +config.get('apikey')
    return hashlib.md5(key .encode()).hexdigest()


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/api/v1.0/marvel", methods=['GET'])
def marvel():
    url=''+config.get('urlbase')+'/comics?ts='+str(convert_ticks())+'&apikey='+config.get('apikey')+'&hash='+generatadmd5()+'&limit='+config.get('limit')+''
    res = requests.get(url)
    return  str(res.json())

@app.route("/api/v1.0/marvel/<heroname>", methods=['GET'])
def marvelhero(heroname):
    url=''+config.get('urlbase')+'/characters?ts='+str(convert_ticks())+'&apikey='+config.get('apikey')+'&hash='+generatadmd5()+'&name='+heroname+''
    print(url)
    res = requests.get(url)
    return  str(res.json())

@app.route("/api/v1.0/marvel", methods=['POST'])
def marvelPost():
    if not Flask.json or not 'title' in Flask.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': Flask.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)
