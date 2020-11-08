from flask_sqlalchemy import SQLAlchemy
from init import app


db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)

