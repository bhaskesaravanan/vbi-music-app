from models.models import User
from init import db
import logging
from uuid import uuid4
from traceback import format_exc
from datetime import datetime


class UserServices(object):
    @classmethod
    def save_user(cls, user_name, password):
        try:
            user = User(
                _id=str(uuid4()),
                username=user_name,
                password=password,
                created=datetime.now(),
                updated=datetime.now()
            )
            db.session.add(user)
            db.session.commit()
            logging.info(user)
            logging.info(user.__repr__())
            return True, 'dfdf'
        except Exception as e:
            logging.info(format_exc())
            return False, ''

    @classmethod
    def fetch_user(cls, user_name):
        try:
            user = User.query.filter_by(username=user_name).first()
            return user
        except Exception as e:
            logging.info(format_exc())
            return False
