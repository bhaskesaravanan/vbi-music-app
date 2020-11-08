from init import db
import logging
from uuid import uuid4
from models.models import Songs
from datetime import datetime
from services.playlist_services import PlayListServices
import constant
import traceback


class SongServices(object):
    @classmethod
    def fetch_songs(cls, playlist_id=None):
        if playlist_id:
            return cls.fetch_songs_by_playlist_id(playlist_id)

        songs = Songs.query.filter_by().all()
        list_of_songs = ([song.serialize() for song in songs])
        list_of_songs = list_of_songs or constant.song_list
        return list_of_songs


    @classmethod
    def fetch_song_by_id(cls, song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if not song:
            song = cls.filter_song(song_id)
            if song:
                return song
            else:
                return []
        return song.serialize()

    @classmethod
    def filter_song(cls, song_id):
        song = None
        for song in constant.song_list:
            if(song.get('id') == song_id):
                song=song
                break
        return song

    @classmethod
    def save_song(cls, title, artist, album, duration):
        try:
            song = Songs(
                _id=str(uuid4()),
                title=title,
                artist=artist,
                album=album,
                duration=duration,
                created=datetime.now(),
                updated=datetime.now()
            )
            db.session.add(song)
            db.session.commit()
            return True, song.__repr__()
        except Exception as e:
            logging.info(traceback.format_exc())
            return False, []

    @classmethod
    def fetch_songs_by_playlist_id(cls, playlist_id):
        list_of_playlist_songs = PlayListServices.fetch_songs_for_playlist(playlist_id)
        song_list = []
        for song in list_of_playlist_songs:
            song = cls.fetch_song_by_id(song.get('song_id'))
            logging.info(song)
            if not song:
                continue
            song_list.append(song)
        return song_list
