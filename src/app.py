# USED FOR TESTING DURING DEVELOPMENT
# DO NOT EXPOSE IN PROD


from flask_app import app

from flask import render_template
from flask_app.models.user import User
from flask_app.models.coffee_drink import CoffeeDrink

@app.route('/')
@app.route('/home')
def home():
    # user = User.get_user('zoon@gmail.com')
    # coffee_drinks = CoffeeDrink.get_coffee_drinks_for_user(user)
    # coffee_drinks = coffee_drinks if coffee_drinks else []
    coffee_drinks = []
    return render_template('home.html', coffee_drinks=coffee_drinks, title='CoffeeLog Flask App')

@app.route('/about')
def about():
    return render_template('about.html', title='CoffeeLog About')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))

#     form = RegistrationForm(request.form)
#     if form.validate_on_submit():
#         user = User(email=form.email.data, password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)

#         flash(f'Account created for {form.email.data}!', category='SUCCESS')
#         return redirect(url_for('home'))

#     return render_template('register.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))

#     form = LoginForm(request.form)
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, request.form['password']):
#             login_user(user)
#             return redirect(url_for('home'))
#         flash('Invalid email or password', category='FAILURE')
#         return render_template('login.html', form=form)
#     return render_template('login.html', form=form)

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('Successfully logged out', category='SUCCESS')
#     return redirect(url_for('login'))

if __name__ == "__main__":
    app.run()
