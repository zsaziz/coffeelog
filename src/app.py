from flask import Flask, render_template, url_for
# from forms import RegistrationForm, LoginForm
import secrets

from data.coffee_drink import CoffeeDrink
from data.coffee_beans import CoffeeBeans

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

USER = 'zoon'

coffee_drinks = [
    CoffeeDrink(USER, 'espresso', 6).to_dict(),
    CoffeeDrink(
        USER, 'drip', 12,
        coffee_beans=CoffeeBeans('Fresh Flours', 'Guatemala', roast_level=5)
        ).to_dict()
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', coffee_drinks=coffee_drinks, title='CoffeeLog Flask App')

@app.route('/about')
def about():
    return render_template('about.html', title='CoffeeLog About')

# @app.route('register')
# def register():
#     form = RegistrationForm()

if __name__ == "__main__":
    app.run()
