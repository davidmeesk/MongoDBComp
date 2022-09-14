from flask import current_app, request
from app import db
from pokemon import app
import numpy as np 
import json

@app.route('/adjust', methods=['GET'])
def set_pokemon():
    results = db.engine.execute("""
        UPDATE pokemon
            SET species_id = S.id
        FROM species S
        WHERE pokemon.species_name = S.name; 
    """)
    results2 = db.engine.execute("""
        ALTER TABLE pokemon
        DROP COLUMN species_name; 
    """)
    response = {
        }
    return json.dumps(response)

# JOGADORES + ALTOS

@app.route('/tallest', methods=['GET'])
def get_tallest_players():
    results = db.engine.execute("""
        SELECT player, height
        FROM players_info
        ORDER BY height DESC
        LIMIT 1
    """)
    for result in results:
        response = {
            "name": result[0],
            "height": result[1] 
        }
    return json.dumps(response)

