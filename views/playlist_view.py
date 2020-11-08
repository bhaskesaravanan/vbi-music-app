from flask import Blueprint, request, jsonify

PLAYLIST_VIEW = Blueprint(
    'playlist_views',
    __name__,
    template_folder='templates'
)


@PLAYLIST_VIEW.route('/api/playlists', methods=['POST'])
def save_playlist():
    payload = request.get_json(force=True)
    user_id = payload.get('user_id')
    playlist_name = payload.get('playlist_name')

    return jsonify(
        {
        'success': True,
        'playlist': {
          "id": '2345453',
          "name": playlist_name,
          "created_date": "24/7/2020"
        }
    })


@PLAYLIST_VIEW.route('/api/playlists')
def fetch_playlist():
    payload = request.args.get('user_id')
    playlist_response = [{
            "id":'2345452',
            "name": "playList1",
            "created_date": "24/5/2020"
        },
        {
            "id":'2345452',
            "name": "playList2",
            "created_date": "24/6/2020"
        },
        {
            "id":'2345452',
            "name": "playList3",
            "created_date": "24/7/2020"
        },
        {
            "id":'2345452',
            "name": "playList3",
            "created_date": "24/7/2020"
        },
        {
            "id":'2345452',
            "name": "playList3",
            "created_date": "24/7/2020"
        },
        {
            "id":'2345452',
            "name": "playList3",
            "created_date": "24/7/2020"
        },
        {
            "id":'2345453',
            "name": "playList3",
            "created_date": "24/7/2020"
        }
    ]
    return jsonify({
        'success': True,
        'playlists':playlist_response
    })

@PLAYLIST_VIEW.route('/api/playlists', methods=["PUT"])
def delete_playlist():
    payload = request.args.get('user_id')
    return jsonify({
        'success': True
    })


@PLAYLIST_VIEW.route('/api/playlists/song', methods=['POST'])
def add_songs_to_playlist():
    payload = request.get_json(force=True)
    user_id = payload.get('user_id')
    playlist_name = payload.get('playlist_id')
    song_id = payload.get('song_id')
    return jsonify({
        'success': True,
    })


@PLAYLIST_VIEW.route('/api/playlists/song', methods=['PUT'])
def delete_songs_to_playlist():
    payload = request.get_json(force=True)
    user_id = payload.get('user_id')
    playlist_name = payload.get('playlist_id')
    song_id = payload.get('song_id')
    return jsonify({
        'success': True,
    })