from init import db
import logging
from uuid import uuid4
from models.models import Songs
from datetime import datetime
import traceback


class SongServices(object):
    @classmethod
    def fetch_songs(cls):
        songs = Songs.query.filter_by().all()
        list_of_songs = ([song.serialize() for song in songs])
        logging.info(list_of_songs)
        return list_of_songs

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
