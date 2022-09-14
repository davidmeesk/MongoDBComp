from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_pymongo import PyMongo

db = PyMongo()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['MONGO_URI'] = "mongodb://localhost:27017/pokemon"
    db.init_app(app)
    migrate.init_app(app, db)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
