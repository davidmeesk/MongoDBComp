from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/pokemon"

mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=['GET'])
def get_pokedex():
    pok = mongo.db.pokemon.find()
    list_cur = list(pok)
    json_data = dumps(list_cur)
    return json_data