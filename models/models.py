from google.cloud import ndb


class Songs(ndb.Model):
    title = ndb.StringProperty()
    artist = ndb.StringProperty()
    album = ndb.StringProperty()
    duration = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateProperty(auto_now=True)


class Playlist(ndb.Model):
    name = ndb.StringProperty()
    user_id = ndb.StringProperty(required=True)
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateProperty(auto_now=True)


class PlayListSongs(ndb.Model):
    playlist_id = ndb.StringProperty()
    song_id = ndb.StringProperty()
    user_id = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateProperty(auto_now=True)


class User(ndb.Model):
    user_email = ndb.StringProperty()
    password = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateProperty(auto_now=True)
