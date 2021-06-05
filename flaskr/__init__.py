from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # default configurations
    app.config.from_object('config.Config')

    # bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


    with app.app_context():
        #blueprint registration
        from .main import main as main_bp
        app.register_blueprint(main_bp)

        from .auth import auth as auth_bp
        app.register_blueprint(auth_bp)
        #creating database
        db.create_all()

        return app
