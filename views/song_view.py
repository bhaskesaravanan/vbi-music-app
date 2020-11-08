from flask import Blueprint, request, jsonify
from main import app

SONG_VIEW = Blueprint(
    'song_views',
    __name__,
    template_folder='templates'
)
app.register_blueprint(SONG_VIEW)


@SONG_VIEW.route('/api/songs')
def save_playlist():
    play_list_id = request.args.get('playlist_id')
    user_id = request.args.get('user_id')
    song_list = [
        {
            "id": "2342394",
            "title": "aut ipsam quos ab placeat omnis",
            "album": "Surai potru",
            "artist": "surya",
            "duration": "3:45"
        },
        {
            "id": "2342304",
            "title": "aut ipsam quos ab placeat omnis",
            "album": "Jigarthada",
            "artist": "surya",
            "duration": "3:45"
        },
        {
            "id": "2342384",
            "title": "voluptate voluptates sequi",
            "album": "papnasam",
            "artist": "Kamlahasan",
            "duration": "3:45"
        },{
            "id": "2342344",
            "title": "ad enim dignissimos voluptatem similique",
            "album": "villain",
            "artist": "Ajith",
            "duration": "3:45"
        },{
            "id": "2342134",
            "title": "voluptate voluptates sequi",
            "album": "sudhukavum",
            "artist": "Vijay sethupathi",
            "duration": "3:45"
        },{
            "id": "2342324",
            "title": "aut ipsam quos ab placeat omnis",
            "album": "Ayirathil oruvan",
            "artist": "Vijay sethupathi",
            "duration": "3:45"
        },{
            "id": "234434",
            "title": "aut ipsam quos ab placeat omnis",
            "album": "Ayirathil oruvan",
            "artist": "Vijay sethupathi",
            "duration": "3:45"
        }
    ]

    return jsonify({
        'success': True,
        'song_list': song_list
    })

