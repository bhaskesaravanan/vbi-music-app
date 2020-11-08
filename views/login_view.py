from flask import Blueprint, render_template, request, jsonify
from services.user_services import UserServices
import logging

LOGIN_VIEW = Blueprint(
    'login_pages',
    __name__,
    template_folder='templates'
)


@LOGIN_VIEW.route('/')
def index():
    return render_template('index.html')


@LOGIN_VIEW.route('/signup', methods=['POST'])
def signup():
    payload=request.get_json(force=True)
    user_name = payload.get('user_name')
    password = payload.get('password')
    user_success, user_id = UserServices.save_user(user_name=user_name, password=password)
    return jsonify({
        'success': user_success,
        'user_id': user_id
    })

@LOGIN_VIEW.route('/login')
def login():
    username=request.args.get('username')
    password=request.args.get('password')
    user = UserServices.fetch_user(user_name=username)
    logging.info(user.username)

    return jsonify({
        'success': True
    })
