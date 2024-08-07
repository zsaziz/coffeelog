from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from flask_app.models.user import User


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(message=None), Length(min=6, max=50)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate(self, extra_validators=None):
        initial_validation = super(RegistrationForm, self).validate()
        if not initial_validation:
            return False

        user = User.get_user(self.email.data)
        if user:
            self.email.errors.append('Email already registered') # type: ignore
            return False
        if self.password.data != self.confirm_password.data:
            self.password.errors.append('Passwords must match') # type: ignore
            return False
        return True
