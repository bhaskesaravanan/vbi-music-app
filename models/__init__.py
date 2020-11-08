# from google.cloud import ndb

from main import db
#
# client = ndb.Client()
#
#
# def ndb_wsgi_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         with client.context():
#             return wsgi_app(environ, start_response)
#     return middleware


from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)
