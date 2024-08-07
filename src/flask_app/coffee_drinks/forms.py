# 3p lib
from flask_wtf import FlaskForm
from wtforms import DateTimeLocalField, FieldList, FormField, IntegerField, SelectField, StringField
from wtforms.validators import DataRequired, Optional

# local lib
from data.coffee_beans import CoffeeBeans
from flask_app.models.coffee_drink import CoffeeDrink

class CoffeeBeansForm(FlaskForm):
    producer = StringField(CoffeeBeans.PRODUCER, validators=[DataRequired()])
    country_of_origin = StringField(CoffeeBeans.COFFEE_BEANS_NAME, validators=[DataRequired()])

    # Optional fields
    beans_name = StringField(CoffeeBeans.NAME)
    roast_level = IntegerField(CoffeeBeans.ROAST_LEVEL)
    flavor_notes = FieldList(StringField(CoffeeBeans.FLAVOR_NOTES), min_entries=3)
    roast_date = DateTimeLocalField(CoffeeBeans.ROAST_DATE)

    def validate(self, extra_validators=None):
        initial_validation = super(CoffeeBeansForm, self).validate()
        if not initial_validation:
            return False
        return True

class CreateCoffeeDrinkForm(FlaskForm):
    drink_name = StringField(CoffeeDrink.DRINK_NAME, validators=[DataRequired()])
    quantity_in_fl_oz = IntegerField(CoffeeDrink.QUANTITY_IN_FL_OZ, validators=[DataRequired()])
    
    # Optional fields
    milk_options = StringField(CoffeeDrink.MILK_OPTIONS, validators=[Optional()])
    additives = FieldList(StringField(CoffeeDrink.ADDITIVES), min_entries=5, validators=[Optional()])
    drink_time = DateTimeLocalField(CoffeeDrink.DRINK_TIME, validators=[Optional()])
    cafe = StringField(CoffeeDrink.CAFE)
    
    # Custom fields
    coffee_beans = FormField(CoffeeBeansForm)

    def validate(self, extra_validators=None):
        initial_validation = super(CreateCoffeeDrinkForm, self).validate()
        if not initial_validation:
            return False
        return True

class CoffeeDrinksHomeForm(FlaskForm):
    sort_order = SelectField('Sort', choices=[('drink_time', 'Drink time'), ('created_time', 'Created time')])

    # In progress
    # ...
    
    def validate(self, extra_validators=None):
        initial_validation = super(CoffeeDrinksHomeForm, self).validate()
        if not initial_validation:
            return False
        return True