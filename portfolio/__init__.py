import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

csrf = CSRFProtect()
mail = Mail()

def create_app():
    app=Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config.from_pyfile('config.py', silent=True)

    csrf.init_app(app)
    mail.init_app(app)

    return app

app= create_app()


from portfolio import route


class Meta():
    csrf=True
    csrf_time_limit=7200