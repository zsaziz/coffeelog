# 3p lib
from flask_login import UserMixin

# local lib
from flask_app import bcrypt, db
from utils.logging_utils import get_logger
from utils.common_utils import get_current_local_datetime

log = get_logger(__name__)


class User(UserMixin, db.Model):
    """Flask DB class object for User metadata.

    Honestly, just stay away from this class :)
    """

    USER_NAME = 'user'
    USER_TABLE_NAME = 'coffeelog-user-metadata'

    EMAIL = 'email'
    PASSWORD = 'password'
    ADMIN_ACCESS = 'admin_access'

    __tablename__ = USER_TABLE_NAME

    email = db.Column(db.String, nullable=False, unique=True, primary_key=True, autoincrement=False)
    password = db.Column(db.String, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    admin_access = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin_access=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_time = get_current_local_datetime()
        self.admin_access = admin_access

    def get_id(self):
        return self.email

    def __repr__(self):
        public_repr = self.__dict__
        del public_repr[self.PASSWORD]
        return f'{public_repr}'
    
    def __str__(self):
        return f'{self.__class__.__name__}/\n{self.__repr__()}'
    
    def validate_password(self, password: str):
        return bcrypt.check_password_hash(self.password, password)

    def create_user(self):
        db.session.add(self)
        db.session.commit()
        log.info(f'Created {User.USER_NAME} {self.email}')

    def update_password(self, password: str):
        self.password = bcrypt.generate_password_hash(password)
        db.session.commit()
        log.info(f'Updated {User.PASSWORD} for {self.email}')

    def update_admin_access(self, admin_access: bool):
        self.admin_access = admin_access
        db.session.commit()
        log.info(f'Updated {User.ADMIN_ACCESS} to {self.admin_access} for {self.email}')


    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
        log.info(f'Deleted {User.USER_NAME} {self.email}')

    @staticmethod
    def get_user(email: str):
        return User.query.get(email)
    
    @staticmethod
    def _delete_all():
        User.query.delete()
        db.session.commit()
        log.info(f'Deleted all {User.USER_NAME}')
