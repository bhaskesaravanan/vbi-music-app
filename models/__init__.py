# from google.cloud import ndb

# from main import db
#
# client = ndb.Client()
#
#
# def ndb_wsgi_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         with client.context():
#             return wsgi_app(environ, start_response)
#     return middleware


# from flask_sqlalchemy import SQLAlchemy
# from main import app
#
# db = SQLAlchemy(app)

# from flask_sqlalchemy import SQLAlchemy

# sql_alchemy = SQLAlchemy()
# engine = sql_alchemy.create_engine("postgresql://postgres:123456@localhost/vbi",{})
# db = sql_alchemy.create_scoped_session(sql_alchemy.create_session(engine))

