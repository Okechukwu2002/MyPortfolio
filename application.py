from flask import Flask
from flask_mongoengine import MongoEngine

# setup db
db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile("settings.py")

    # apply overrides for tests
    app.config.update(config_overrides)

    # initializa db
    db.init_app(app)

    # import blueprints
    
    return app