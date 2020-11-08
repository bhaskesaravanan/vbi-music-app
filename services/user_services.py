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
                id=str(uuid4()),
                username=user_name,
                password=password,
                created=datetime.now(),
                updated=datetime.now()
            )
            db.session.add(user)
            db.session.commit()
            logging.info(user)
            logging.info(user.__repr__())
            return True, user.__repr__()
        except Exception as e:
            logging.info(format_exc())
            return False, ''
