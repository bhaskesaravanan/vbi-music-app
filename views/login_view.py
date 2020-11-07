from flask import Blueprint, render_template

LOGIN_VIEW = Blueprint(
    'login_pages',
    __name__,
    template_folder='templates'
)


@LOGIN_VIEW.route('/')
def index():
    return render_template('index.html')
