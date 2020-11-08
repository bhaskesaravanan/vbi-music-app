from flask import session, jsonify
import logging


def authenticate():
    def method_wrap(method):
        def wrap(self, *args, **kwargs):
            api_key = self.request.headers.get('x-api-key')
            logging.info('api_key : %s', api_key)

            if session['username'] == api_key :
                return method(self, *args, **kwargs)
            else:
                return jsonify({
                    'success': False,
                    'login_required': True
                })

        return wrap
    return method_wrap