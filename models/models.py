from init import db
import logging


class Songs(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())
    artist = db.Column(db.String())
    album = db.Column(db.String())
    duration = db.Column(db.String())
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())

    def __init__(self, _id, title, artist, album, duration, created, updated):
        self.id = _id
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.created = created
        self.updated = updated

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
    __tablename__ = 'playlist'
    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.String())
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())


    def __init__(self, _id, name, user_id, created, updated):
        self.id = _id
        self.name = name
        self.user_id = user_id
        self.created = created
        self.updated = updated

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'created_date': self.created
        }


class PlayListSongs(db.Model):
    __tablename__ = 'playlistitem'
    id = db.Column(db.String(), primary_key=True)
    playlist_id = db.Column(db.String())
    song_id = db.Column(db.String())
    user_id = db.Column(db.String())
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())

    def __init__(self, _id, playlist_id, song_id, user_id, created, updated):
        self.id = _id
        self.playlist_id = playlist_id
        self.song_id = song_id
        self.user_id = user_id
        self.created = created
        self.updated = updated

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
