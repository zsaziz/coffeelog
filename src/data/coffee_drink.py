# 3P lib
from proto.datetime_helpers import DatetimeWithNanoseconds

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

    COFFEE_DRINK_NAME = 'CoffeeDrink'

    BREW_ID = 'brew_id'
    USER_ID = 'user_id'
    DRINK = 'drink'
    QUANTITY_IN_FL_OZ = 'quantity_in_fl_oz'
    MILK_OPTIONS = 'milk_options'
    ADDITIVES = 'additives'
    COFFEE_BEANS = 'coffee_beans'
    CAFE = 'cafe'
    ENTRY_DATETIME = 'entry_datetime'

    def __init__(self,
        user_id: str,
        drink: str,
        quantity_in_fl_oz: int,
        milk_options: Optional[str] = None,
        additives: Optional[List[str]] = None,
        coffee_beans: Optional[CoffeeBeans] = None,
        cafe: Optional[str] = None
    ) -> None:
        if not user_id:
            raise AttributeError(f'User attribute ({CoffeeDrink.USER_ID}) must be present but is empty.')
        if not drink:
            raise MissingArgumentError(self.DRINK)
        if not quantity_in_fl_oz:
            raise MissingArgumentError(self.QUANTITY_IN_FL_OZ)
        
        # Properties
        # ---
        self.user_id = user_id
        self.drink = drink
        self.quantity_in_fl_oz = quantity_in_fl_oz
        self.milk_options = milk_options
        self.additives = additives
        self.coffee_beans = coffee_beans
        self.cafe = cafe

        # Set current date and time in local TZ as datetime object
        self.entry_datetime = get_current_local_datetime()

        # Create and set brew_id - unique identifier for each entity
        self.brew_id = f'{self.user_id}-{self.drink}-{int(self.entry_datetime.timestamp())}'
        # ---

    @staticmethod
    def from_dict(source):
        # Initialize CoffeeDrink class
        coffee_drink = CoffeeDrink(source[CoffeeDrink.USER_ID], source[CoffeeDrink.DRINK], source[CoffeeDrink.QUANTITY_IN_FL_OZ])
        # Delete set fields from source dictionary
        del source[CoffeeDrink.USER_ID]
        del source[CoffeeDrink.DRINK]
        del source[CoffeeDrink.QUANTITY_IN_FL_OZ]

        # Set remaining attributes in source dictionary to class
        for key, val in source.items():
            if key == CoffeeDrink.COFFEE_BEANS and val:
                setattr(coffee_drink, key, CoffeeBeans.from_dict(val))
            elif key == CoffeeDrink.ENTRY_DATETIME and isinstance(val, DatetimeWithNanoseconds):
                localized_datetime = datetime.fromtimestamp(val.timestamp(), val.tzinfo).astimezone().replace(microsecond=0)
                setattr(coffee_drink, key, localized_datetime)
            else:
                setattr(coffee_drink, key, val)
        return coffee_drink

    def to_dict(self):
        return dict((key, val.to_dict() if isinstance(val, CoffeeBeans) else val) for (key, val) in self.__dict__.items())
