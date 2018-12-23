from flask import Flask, request
from zatt.client import DistributedDict
from json import dumps
import time

app = Flask(__name__)

leader = DistributedDict('127.0.0.1', 5254)
fol1 = DistributedDict('127.0.0.1', 5255)
fol2 = DistributedDict('127.0.0.1', 5256)
@app.route('/showleader', methods=['GET'])
def show():
	return dumps(leader['key1'])

@app.route('/showfollower1', methods=['GET'])
def show1():
	return dumps(fol1['key1'])

@app.route('/showfollower2', methods=['GET'])
def show2():
	return dumps(fol2['key1'])

@app.route('/set/<arg>', methods=['POST'])
def set(arg):
	leader['key1']=arg
	return dumps('Berhasil')

if __name__ == '__main__':
	app.run(debug=True)
