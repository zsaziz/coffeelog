# local lib
from data.coffee_base import CoffeeBase
from data.coffee_beans import CoffeeBeans

# python lib
from typing import List, Optional

class UpdateCoffeeDrink(CoffeeBase):
    """Local class object for updating CoffeeDrink data
    """

    UPDATE_COFFEE_DRINK_NAME = 'UpdateCoffeeDrink'

    DRINK_NAME = 'drink_name'
    QUANTITY_IN_FL_OZ = 'quantity_in_fl_oz'
    MILK_OPTIONS = 'milk_options'
    ADDITIVES = 'additives'
    COFFEE_BEANS = 'coffee_beans'
    CAFE = 'cafe'

    def __init__(self, *,
        drink_name: Optional[str] = None,
        quantity_in_fl_oz: Optional[int] = None,
        milk_options: Optional[str] = None,
        additives: Optional[List[str]] = None,
        coffee_beans: Optional[CoffeeBeans] = None,
        cafe: Optional[str] = None
    ) -> None:

        # Properties
        # ---
        self.drink_name = drink_name
        self.quantity_in_fl_oz = quantity_in_fl_oz
        self.milk_options = milk_options
        self.additives = additives
        self.coffee_beans = coffee_beans
        self.cafe = cafe
        # ---
    
    @staticmethod
    def from_dict(source):
        # Initialize UpdateCoffeeDrink class
        coffee_drink = UpdateCoffeeDrink()

        # Set attributes in source dictionary to class
        for key, val in source.items():
            if key == UpdateCoffeeDrink.COFFEE_BEANS and val:
                setattr(coffee_drink, key, CoffeeBeans.from_dict(val))
            else:
                setattr(coffee_drink, key, val)
        return coffee_drink

    def to_dict(self):
        return dict((key, val.to_dict() if isinstance(val, CoffeeBeans) else val) for (key, val) in self.__dict__.items())
