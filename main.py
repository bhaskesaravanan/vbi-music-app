import os
import sys
import logging
from uuid import uuid4
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from views.login_view import LOGIN_VIEW
from views.playlist_view import PLAYLIST_VIEW
from views.song_view import SONG_VIEW

app = Flask(__name__)
# app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)
logging.basicConfig(level=logging.INFO)

Env = 'dev'
if Env == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/vbi'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

root_path = os.path.abspath('.')
sys.path.insert(0, root_path)
app.static_folder = os.path.join(app.root_path, "static")

app.register_blueprint(LOGIN_VIEW)
app.register_blueprint(PLAYLIST_VIEW)
app.register_blueprint(SONG_VIEW)


if __name__ == '__main__':
    app.run(debug=True)

