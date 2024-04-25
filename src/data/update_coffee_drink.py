# local lib
from data.coffee_drink import CoffeeDrink
from data.coffee_beans import CoffeeBeans

# python lib
from typing import List, Optional

class UpdateCoffeeDrink(CoffeeDrink):
    """Local class object for updating CoffeeDrink data
    """

    def __init__(self, *,
        quantity_in_fl_oz: Optional[int] = None,
        milk_options: Optional[str] = None,
        additives: Optional[List[str]] = None,
        coffee_beans: Optional[CoffeeBeans] = None,
        cafe: Optional[str] = None
    ) -> None:

        # Properties
        # ---
        self.quantity_in_fl_oz = quantity_in_fl_oz
        self.milk_options = milk_options
        self.additives = additives
        self.coffee_beans = coffee_beans
        self.cafe = cafe
        # ---
