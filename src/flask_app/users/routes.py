# 3p lib
from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required, login_user, logout_user

# local lib
from flask_app import bcrypt, db
from flask_app.users.forms import LoginForm, RegistrationForm
from flask_app.constants import HTTPMethods
from flask_app.models.user import User

users_bp = Blueprint("users", __name__)

REDIRECT_FALLBACK_DEFAULT = 'drinks'

@users_bp.route('/register', methods=[HTTPMethods.GET, HTTPMethods.POST])
def register():
    if current_user.is_authenticated:
        return redirect_dest()

    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        user.create_user()
        login_user(user)

        flash(f'Account created for {user.email}!', category='SUCCESS')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

@users_bp.route('/login', methods=[HTTPMethods.GET, HTTPMethods.POST])
def login():
    if current_user.is_authenticated:
        return redirect_dest()

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.get_user(form.email.data)
        if user and user.validate_password(form.password.data):
            login_user(user)
            return redirect_dest()
        flash('Invalid email or password', category='FAILURE')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out', category='SUCCESS')
    return redirect(url_for('users.login'))

def redirect_dest(fallback=REDIRECT_FALLBACK_DEFAULT):
    dest = request.args.get('drinks')
    try:
        dest_url = url_for(dest)
    except:
        return redirect(fallback)
    return redirect(dest_url)
