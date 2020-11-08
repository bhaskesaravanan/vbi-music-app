from views.login_view import LOGIN_VIEW
from views.playlist_view import PLAYLIST_VIEW
from views.song_view import SONG_VIEW


def register_blueprints(app):
    app.register_blueprint(LOGIN_VIEW)
    app.register_blueprint(PLAYLIST_VIEW)
    app.register_blueprint(SONG_VIEW)