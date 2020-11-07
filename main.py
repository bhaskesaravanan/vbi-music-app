import os
import sys
import logging
from uuid import uuid4
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy



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


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/api/playlists', methods=['POST'])
# def save_playlist():
#     payload = request.get_json(force=True)
#     logging.info(payload)
#     playlist = Playlist(
#         id=str(uuid4()),
#         name=payload.get('name'),
#         user_id=payload.get('user_id')
#     ).put()
#
#     logging.info(playlist)
#     return jsonify({
#         'success': True,
#         'playlist_id': playlist.id()
#     })
#
# @app.route('/api/playlists')
# def fetch_playlist():
#     playList = Playlist.query().fetch()
#     logging.info(playList)
#     return jsonify({
#         'success': True
#     })

if __name__ == '__main__':
    app.run(debug=True)

