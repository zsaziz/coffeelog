from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_app.config import DevelopmentConfig

app = Flask(__name__)
# app.config['SECRET_KEY'] = secrets.token_hex()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config.from_object(DevelopmentConfig())

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

from flask_app.models.user import User

login_manager.login_view = 'login'
login_manager.login_message_category = 'DANGER'

@login_manager.user_loader
def load_user(user_email):
    return User.get_user(user_email)

from flask_app.users.routes import users_bp
from flask_app.coffee_drinks.routes import coffee_drinks_bp
# Registering blueprints
app.register_blueprint(users_bp)
app.register_blueprint(coffee_drinks_bp)