# local lib
from data.coffee_drink import CoffeeDrink
from flask_app import db


class AdditivesJsonEncoder(db.TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = db.JSON

    def process_bind_param(self, value, dialect):
        if value:
            return {CoffeeDrink.ADDITIVES: value}
        return {CoffeeDrink.ADDITIVES: []}
        
    def process_result_value(self, value, dialect):
        if value:
            return value.get(CoffeeDrink.ADDITIVES)
        return []
