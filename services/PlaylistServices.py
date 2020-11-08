from main import db
import logging
from models.models import Playlist, PlayListSongs

class PlayListServides(object):

    @classmethod
    def fetch_playlist_for_user(cls, user_id):
        playlists = Playlist.query.filter_by(user_id=user_id).all()
        list_of_playlist = ([playlist.serialize() for playlist in playlists])
        logging.info(list_of_playlist)
        return list_of_playlist

    @classmethod
    def save_playlist(cls, playlist_name, user_id):
        playlist = Playlist(
            name=playlist_name,
            user_id=user_id
        )
        db.session.add(playlist)
        db.session.commit()
        return playlist.__repr__()

    @classmethod
    def delete_playlist(cls, playlist_id):
        playlist = Playlist.query.filter_by(id=playlist_id).first()
        db.session.delete(playlist)
        db.session.commit()

    def playlist_songs_by_playlist_id(self, playlist_id, user_id):
        playlists = PlayListSongs.query.filter_by(playlist_id=playlist_id).all()
        for playlist in playlists:
            db.session.delete(playlist)
        db.session.commit()
