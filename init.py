import os
import sys
import logging
from uuid import uuid4
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import heroku


app = Flask(__name__)
app.secret_key = 'qwertyuioplkjhgfdsazxcvbnm'
root_path = os.path.abspath('.')
sys.path.insert(0, root_path)
app.static_folder = os.path.join(app.root_path, "static")
db = SQLAlchemy(app)

logging.basicConfig(level=logging.INFO)

Env = 'live'
if Env == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/vbi'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = heroku.db_config

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import routes
