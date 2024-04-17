# local lib
from data.coffee_base import CoffeeBase
from data.coffee_beans import CoffeeBeans
from exceptions.missing_argument_error import MissingArgumentError
from utils.common_utils import get_current_local_datetime

# python lib
from datetime import datetime, timezone
from typing import List, Optional
import inspect

class CoffeeDrink(CoffeeBase):
    """Local class object for CoffeeDrink data
    """

    COFFEE_DRINK_NAME = "CoffeeDrink"

    DRINK = "drink"
    QUANTITY_IN_FLUID_OZ = "quantity_in_fluid_oz"
    MILK_OPTIONS = "milk_options"
    ADDITIVES = "additives"
    COFFEE_BEANS = "coffee_beans"
    CAFE = "cafe"
    ENTRY_DATETIME = "entry_datetime"

    def __init__(self,
        drink: str,
        quantity_in_fluid_oz: int,
        milk_options: Optional[str] = None,
        additives: Optional[List[str]] = None,
        coffee_beans: Optional[CoffeeBeans] = None,
        cafe: Optional[str] = None
    ) -> None:
        if not drink:
            raise MissingArgumentError(self.DRINK)
        if not quantity_in_fluid_oz:
            raise MissingArgumentError(self.QUANTITY_IN_FLUID_OZ)
        
        self.drink = drink
        self.quantity_in_fluid_oz = quantity_in_fluid_oz
        self.milk_options = milk_options
        self.additives = additives
        self.coffee_beans = coffee_beans
        self.cafe = cafe

        # Set current date and time in local TZ as datetime object
        self.entry_datetime = get_current_local_datetime()

    @staticmethod
    def from_dict(source):
        # Initialize CoffeeDrink class
        coffee_drink = CoffeeDrink(source[CoffeeDrink.DRINK], source[CoffeeDrink.QUANTITY_IN_FLUID_OZ])
        # Delete set fields from source dictionary
        del source[CoffeeDrink.DRINK]
        del source[CoffeeDrink.QUANTITY_IN_FLUID_OZ]

        # Set remaining attributes in source dictionary to class
        for key, val in source.items():
            if key == CoffeeDrink.COFFEE_BEANS:
                setattr(coffee_drink, key, CoffeeBeans.from_dict(val))
            else:
                setattr(coffee_drink, key, val)
        return coffee_drink

    def to_dict(self):
        return dict((key, val.to_dict() if isinstance(val, CoffeeBeans) else val) for (key, val) in self.__dict__.items())