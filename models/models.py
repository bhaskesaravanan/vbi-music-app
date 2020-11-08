from models import db

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
    __tablename__ = 'User'
    user_name = db.Column(db.String())
    password = db.Column(db.String())
    # created_date = ndb.DateTimeProperty(auto_now_add=True)
    # updated_date = ndb.DateProperty(auto_now=True)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'password': self.password
        }
