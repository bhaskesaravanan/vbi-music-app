from init import db
import logging

class Songs(db.Model):
    __tablename__ = 'Songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    artist = db.Column(db.String())
    album = db.Column(db.String())
    duration = db.Column(db.String())
    # created_date = ndb.DateTimeProperty(auto_now_add=True)
    # updated_date = ndb.DateProperty(auto_now=True)

    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'duration': self.duration
        }

    @classmethod
    def save_user(cls, user_name, password):
        try:
            user = User(
                user_name=user_name,
                password=password
            )
            db.session.add(user)
            db.session.commit()
            logging.info(user)
            logging.info(user.__repr__())
            return True, user.__repr__()
        except Exception as e:
            logging.info(format_exc())
            return False, ''


class Playlist(db.Model):
    __tablename__ = 'Playlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.String())
    # created_date = ndb.DateTimeProperty(auto_now_add=True)
    # updated_date = ndb.DateProperty(auto_now=True)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
        }


class PlayListSongs(db.Model):
    __tablename__ = 'PlaylistSongs'
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.String())
    song_id = db.Column(db.String())
    user_id = db.Column(db.String())
    # created_date = ndb.DateTimeProperty(auto_now_add=True)
    # updated_date = ndb.DateProperty(auto_now=True)

    def __init__(self, playlist_id, song_id, user_id):
        self.playlist_id = playlist_id
        self.song_id = song_id
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'song_id': self.song_id,
            'user_id': self.user_id,
            'playlist_id': self.playlist_id
        }


class User(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    created= db.Column(db.DateTime())
    updated = db.Column(db.DateTime())

    def __init__(self, _id, username, password, created, updated):
        self.id = _id
        self.username = username
        self.password = password
        self.created = created
        self.updated = updated

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
