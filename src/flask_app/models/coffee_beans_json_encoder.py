# local lib
from data.coffee_beans import CoffeeBeans
from flask_app import db


class CoffeeBeansJsonEncoder(db.TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = db.JSON

    def process_bind_param(self, value, dialect):
        if value:
            return value.to_dict()
        return None
        
    def process_result_value(self, value, dialect):
        if value:
            return CoffeeBeans.from_dict(value)
        return None
