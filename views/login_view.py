from flask import Blueprint, session, render_template, request, jsonify
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
    if(user_success):
        session['username'] = user_name
    return jsonify({
        'success': user_success,
        'user_id': user_id
    })


@LOGIN_VIEW.route('/login')
def login():
    payload=request.get_json(force=True)
    username=payload.get('username')
    password=payload.get('password')
    user = UserServices.fetch_user(user_name=username)
    logging.info(user.username)
    success = False
    if user.password == password:
        session['username'] = user.id
        success = True
    return jsonify({
        'success': success,
        'user_id': user.id
    })


@LOGIN_VIEW.route('/logout')
def logout():
    payload=request.get_json(force=True)
    username=payload.get('user_id')
    session.pop('username', None)
    return jsonify({
        'success': True
    })
