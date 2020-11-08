from flask import Blueprint, request, jsonify
from services.playlist_services import PlayListServices
import logging

from helper import authenticate

PLAYLIST_VIEW = Blueprint(
    'playlist_views',
    __name__,
    template_folder='templates'
)


@authenticate()
@PLAYLIST_VIEW.route('/api/playlists', methods=['POST'])
def save_playlist():
    payload = request.get_json(force=True)
    user_id = payload.get('user_id')
    playlist_name = payload.get('playlist_name')
    playlist = PlayListServices.save_playlist(playlist_name, user_id)
    logging.info(playlist)
    return jsonify(
        {
        'success': True,
        'playlist': playlist
    })

@authenticate()
@PLAYLIST_VIEW.route('/api/playlists')
def fetch_playlist():
    user_id = request.args.get('user_id')
    playlist_response = PlayListServices.fetch_playlist_for_user(user_id=user_id)
    logging.info(playlist_response)
    return jsonify({
        'success': True,
        'playlists':playlist_response
    })


@authenticate()
@PLAYLIST_VIEW.route('/api/playlists', methods=["PUT"])
def delete_playlist():
    payload = request.args.get('user_id')
    playlist_id = request.args.get('playlist_id')
    response = PlayListServices.delete_playlist(playlist_id)
    return jsonify({
        'success': response
    })


@authenticate()
@PLAYLIST_VIEW.route('/api/playlists/song', methods=['POST'])
def add_songs_to_playlist():
    payload = request.get_json(force=True)
    user_id = payload.get('user_id')
    playlist_id = payload.get('playlist_id')
    song_id = payload.get('song_id')
    success, playlist_response = PlayListServices.add_songs_to_playlist(song_id, playlist_id, user_id)
    return jsonify({
        'success': success,
        'playlist_response': playlist_response
    })


@authenticate()
@PLAYLIST_VIEW.route('/api/playlists/song', methods=['PUT'])
def delete_songs_to_playlist():
    payload = request.get_json(force=True)
    user_id = payload.get('user_id')
    playlist_id = payload.get('playlist_id')
    song_id = payload.get('song_id')
    success: PlayListServices.delete_songs_from_playlist(song_id, playlist_id)
    return jsonify({
        'success': True,
    })
