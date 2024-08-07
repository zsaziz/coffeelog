# local lib
from data.coffee_base import CoffeeBase
from data.coffee_beans import CoffeeBeans
from exceptions.missing_argument_error import MissingArgumentError

# python lib
from typing import List, Optional
from datetime import datetime

class CreateCoffeeDrink(CoffeeBase):
    """Local class object for CreateCoffeeDrink data
    """

    CREATE_COFFEE_DRINK_NAME = 'CreateCoffeeDrink'

    DRINK_NAME = 'drink_name'
    QUANTITY_IN_FL_OZ = 'quantity_in_fl_oz'
    MILK_OPTIONS = 'milk_options'
    ADDITIVES = 'additives'
    COFFEE_BEANS = 'coffee_beans'
    CAFE = 'cafe'
    DRINK_TIME = 'drink_time'

    def __init__(self,
        drink_name: str,
        quantity_in_fl_oz: int,
        milk_options: Optional[str] = None,
        additives: Optional[List[str]] = None,
        coffee_beans: Optional[CoffeeBeans] = None,
        cafe: Optional[str] = None,
        drink_time: Optional[datetime] = None,
    ) -> None:
        if not drink_name:
            raise MissingArgumentError(self.DRINK_NAME)
        if not quantity_in_fl_oz:
            raise MissingArgumentError(self.QUANTITY_IN_FL_OZ)
        
        # Properties
        # ---
        self.drink_name = drink_name
        self.quantity_in_fl_oz = quantity_in_fl_oz
        self.milk_options = milk_options
        self.additives = additives
        self.coffee_beans = coffee_beans
        self.cafe = cafe
        self.drink_time = drink_time
        # ---

    @staticmethod
    def from_dict(source):
        # Initialize CreateCoffeeDrink class
        # Pop initialization attributes to get and remove
        coffee_drink = CreateCoffeeDrink(source.pop(CreateCoffeeDrink.DRINK_NAME), source.pop(CreateCoffeeDrink.QUANTITY_IN_FL_OZ))

        # Set remaining attributes in source dictionary to class
        for key, val in source.items():
            if key == CreateCoffeeDrink.COFFEE_BEANS and val:
                setattr(coffee_drink, key, CoffeeBeans.from_dict(val))
            else:
                setattr(coffee_drink, key, val)
        return coffee_drink

    def to_dict(self):
        return dict((key, val.to_dict() if isinstance(val, CoffeeBeans) else val) for (key, val) in self.__dict__.items())
