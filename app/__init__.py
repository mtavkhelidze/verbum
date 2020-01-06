from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .logging_setup import logging_setup


logging_setup()

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from .nlp import NLP


nlp = NLP(app)

from .api import api


app.register_blueprint(api, url_prefix="/api")
