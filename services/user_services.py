from models.models import User
from init import db
import logging
from traceback import format_exc

class UserServices(object):

    @classmethod
    def save_user(cls, user_name, password):
        try:
            user = User(
                username=user_name,
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
