from init import db
import logging
import traceback
from uuid import uuid4
from models.models import Playlist, PlayListSongs
from datetime import datetime


class PlayListServices(object):

    @classmethod
    def fetch_playlist_for_user(cls, user_id):
        playlists = Playlist.query.filter_by(user_id=user_id).all()
        list_of_playlist = ([playlist.serialize() for playlist in playlists])
        logging.info(list_of_playlist)
        return list_of_playlist

    @classmethod
    def save_playlist(cls, playlist_name, user_id):
        playlist = Playlist(
            _id=str(uuid4()),
            name=playlist_name,
            user_id=user_id,
            created=datetime.now(),
            updated=datetime.now()
        )
        db.session.add(playlist)
        db.session.commit()
        return playlist.serialize()

    @classmethod
    def delete_playlist(cls, playlist_id):
        try:
            Playlist.query.filter_by(id=playlist_id).delete()
            db.session.commit()
            cls.playlist_songs_by_playlist_id(playlist_id)
            return True
        except Exception as e:
            logging.info(traceback.format_exc())
            return False

    @classmethod
    def playlist_songs_by_playlist_id(cls, playlist_id):
        playlists = PlayListSongs.query.filter_by(playlist_id=playlist_id).delete()
        # for playlist in playlists:
        #     db.session.delete(playlist)
        db.session.commit()

    @classmethod
    def add_songs_to_playlist(cls, song_id, playlist_id, user_id):
        try:
            playlist_song = PlayListSongs(
                _id=str(uuid4()),
                playlist_id=playlist_id,
                song_id=song_id,
                user_id=user_id,
                created=datetime.now(),
                updated=datetime.now()
            )
            db.session.add(playlist_song)
            db.session.commit()
            return True, playlist_song.serialize()
        except Exception as e:
            logging.info(traceback.format_exc())
            return False, []

    @classmethod
    def delete_songs_from_playlist(cls, song_id, playlist_id):
        try:
            song = PlayListSongs.query.filter_by(
                playlist_id=playlist_id,
                song_id=song_id
            ).first()
            db.session.delete(song)
            db.session.commit()
            return True
        except Exception as e:
            logging.info(traceback.format_exc())
            return False