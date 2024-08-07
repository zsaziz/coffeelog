# 3p lib
from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user

# local lib
from data.coffee_beans import CoffeeBeans
from data.create_coffee_drink import CreateCoffeeDrink
from exceptions.not_authenticated_error import NotAuthenticatedError
from flask_app.coffee_drinks.forms import CoffeeDrinksHomeForm, CreateCoffeeDrinkForm
from flask_app.constants import HTTPMethods
from flask_app.models.coffee_drink import CoffeeDrink

coffee_drinks_bp = Blueprint("coffee_drinks", __name__)

@coffee_drinks_bp.before_request
def before_request():
    if not current_user.is_authenticated:
        flash(NotAuthenticatedError().message)
        return redirect(url_for('users.login'))
    
@coffee_drinks_bp.route('/drinks', methods=[HTTPMethods.GET, HTTPMethods.POST])
def coffee_drinks_home():
    form: CoffeeDrinksHomeForm = CoffeeDrinksHomeForm(request.form)
    coffee_drinks = CoffeeDrink.get_coffee_drinks_for_user(current_user)
    coffee_drinks = coffee_drinks if coffee_drinks else []
    if form.validate_on_submit():
        sort_order = form.sort_order.data

        coffee_drinks = CoffeeDrink.get_coffee_drinks_for_user(current_user, sort_order)
        coffee_drinks = coffee_drinks if coffee_drinks else []

        return render_template('drinks_home.html', form=form, coffee_drinks=coffee_drinks)


    return render_template('drinks_home.html', form=form, coffee_drinks=coffee_drinks)

@coffee_drinks_bp.route('/drinks/add', methods=[HTTPMethods.GET, HTTPMethods.POST])
def add_drink():
    form: CreateCoffeeDrinkForm = CreateCoffeeDrinkForm(request.form)
    coffee_beans = None
    if form.validate_on_submit():
        coffee_beans_dict = form.coffee_beans.data
        if coffee_beans_dict.get('producer', None) and coffee_beans_dict.get('country_of_origin', None):
            # coffee_beans = CoffeeBeans(
            #     producer=form.coffee_beans.producer.data,
            #     country_of_origin=form.coffee_beans.country_of_origin.data,
            #     beans_name=form.coffee_beans.beans_name.data,
            #     roast_level=form.coffee_beans.roast_level.data,
            #     flavor_notes=form.coffee_beans.flavor_notes.data,
            #     roast_date=form.coffee_beans.roast_date.data,
            # )
            coffee_beans = CoffeeBeans.from_dict(coffee_beans_dict)
                

        def remove_dupes_from_list_with_order(dupe_list):
            seen = set()
            seen_add = seen.add
            return [item for item in form.additives.data if not (item in seen or seen_add(item))]

        create_coffee_drink = CreateCoffeeDrink(
            drink_name=form.drink_name.data,
            quantity_in_fl_oz=form.quantity_in_fl_oz.data,
            milk_options=form.milk_options.data,
            additives=remove_dupes_from_list_with_order(form.additives.data),
            coffee_beans=coffee_beans,
            drink_time=form.drink_time.data
        )

        coffee_drink = CoffeeDrink(create_coffee_drink, current_user.email)
        coffee_drink.create_coffee_drink()
        return redirect(url_for('coffee_drinks.coffee_drinks_home'))
    return render_template('drinks_add.html', form=form)