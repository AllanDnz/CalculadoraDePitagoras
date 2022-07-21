from ast import Num
from collections import UserString
from math import sqrt
from flask.json import jsonify
from flask import Flask, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False



def pitagoras(cateto1, cateto2):
    return sqrt(pow(cateto1, 2) + pow(cateto2, 2))


@app.route("/")
def root():
    return "<h1>api com flask</h1>"

@app.route("/pitagoras", methods=['POST']) 

def hipotenusa():
    print("estou aqui 1")
    catet1 = request.json.get("cateto1")
    catet2 = request.json.get("cateto2")

    print("estou aqui 2 ")

    if catet1<=0 or catet2<=0 :
        return jsonify("something goes wrong"),400

    result= pitagoras(catet1, catet2)
    return jsonify({'result':result}),200
    
app.run(debug=True)