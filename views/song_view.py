from flask import Blueprint, request, jsonify
from services.song_services import SongServices
import logging
import constant

SONG_VIEW = Blueprint(
    'song_views',
    __name__,
    template_folder='templates'
)


@SONG_VIEW.route('/api/songs')
def save_playlist():
    play_list_id = request.args.get('playlist_id')
    user_id = request.args.get('user_id')
    song_list = SongServices.fetch_songs(play_list_id)
    logging.info(song_list)
    return jsonify({
        'success': True,
        'song_list': song_list
    })


@SONG_VIEW.route('/api/songs', methods=['POST'])
def save_song():
    payload = request.get_json(force=True)
    title = payload.get('title')
    artist = payload.get('artist')
    album = payload.get('album')
    duration = payload.get('duration')
    playlist = SongServices.save_song(title, artist, album, duration)
    logging.info(playlist)
    return jsonify({
        'success': True,
        'playlist': playlist
    })
