# USED FOR TESTING DURING DEVELOPMENT
# DO NOT EXPOSE IN PROD

from flask.cli import AppGroup
from data.update_coffee_drink import UpdateCoffeeDrink
from flask_app import app, db

from data.create_coffee_drink import CreateCoffeeDrink
from data.coffee_beans import CoffeeBeans
from flask_app.models.user import User
from flask_app.models.coffee_drink import CoffeeDrink
from flask_app.models.user import User

import click

cli = AppGroup(app)

@cli.command('test_drinks')
@click.argument('d')
def test_drinks(d):
    if d == 'y':
        CoffeeDrink._delete_all()
        # User._delete_all()
        return

    cb = CoffeeBeans('Fresh flours', 'Guatemala')
    ccd = CreateCoffeeDrink('espreso', 6, additives=['vanilla', 'nutmeg'], coffee_beans=cb)
    cd1 = CoffeeDrink(ccd, 'zoon@gmail.com')
    cd1.create_coffee_drink()
    print(cd1.public_dict())
    print(type(cd1.coffee_beans), (cd1.coffee_beans))
    print(type(cd1.additives), (cd1.additives))
    

    print('get')
    cd = CoffeeDrink.get_coffee_drink(cd1.brew_id)

    print(cd)
    print(type(cd.coffee_beans), (cd.coffee_beans))
    print(type(cd.additives), (cd.additives))
    
    ucd = UpdateCoffeeDrink(drink_name='drip')
    cd.update_coffee_drink(ucd)

    cd = CoffeeDrink.get_coffee_drink(cd1.brew_id)

    print(cd)
    print(type(cd.coffee_beans), (cd.coffee_beans))
    print(type(cd.additives), (cd.additives))


@cli.command('test_users')
def test_users():
    User._delete_all()
    user = User('test@gmail.com', 'password', True)
    user.create_user()

    user = User.get_user('test@gmail.com')

    print(user)

    user.update_password('password2')

    print(user)

    user.update_admin_access(False)

    print(user)

    user.delete_user()


if __name__ == "__main__":
    cli()
