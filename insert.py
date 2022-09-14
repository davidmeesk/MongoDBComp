from app import db, create_app
from datetime import datetime
import pymongo
import csv

def feet_and_inches_to_cm(feet, inches):
    return int(round(feet*30.48 + inches*2.54))

def lbs_to_kg(lbs):
    return int(round(lbs * 453.592 / 1000))

def insert_pokemon_species():
    with open("data/pokedex.csv", 'r') as file:
        reader = csv.DictReader( csvfile )
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            db.species.insert(row)

def insert_trainers():
    rows = []
    with open("data/trainers.csv", 'r') as file:
        reader = csv.DictReader( csvfile )
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            db.trainer.insert(row)

def insert_pokemon():
    rows = []
    with open("data/pokemon.csv", 'r') as file:
        reader = csv.DictReader( csvfile )
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            db.pokemon.insert(row)


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    db.create_all()
    insert_pokemon_species()
    insert_trainers()
    insert_pokemon()
    
