# local lib
from data.coffee_base import CoffeeBase
from exceptions.missing_argument_error import MissingArgumentError

# python lib
from datetime import datetime
from typing import List, Optional

class CoffeeBeans(CoffeeBase):
    """Local class object for CoffeeBeans data
    """

    COFFEE_BEANS_NAME = "CoffeeBeans"
    PRODUCER = "producer"
    COUNTRY_OF_ORIGIN = "country_of_origin"
    NAME = "name"
    ROAST_LEVEL = "roast_level"
    FLAVOR_NOTES = "flavor_notes"
    ROAST_DATE = "roast_date"

    def __init__(self,
        producer: str,
        country_of_origin: str,
        name: Optional[str] = None,
        roast_level: Optional[int] = None,
        flavor_notes: Optional[List[str]] = None,
        roast_date: Optional[datetime] = None
    ) -> None:
        if not producer:
            raise MissingArgumentError(self.PRODUCER)
        if not country_of_origin:
            raise MissingArgumentError(self.COUNTRY_OF_ORIGIN)
        
        self.producer = producer
        self.country_of_origin = country_of_origin
        self.name = name
        self.roast_level = roast_level
        self.flavor_notes = flavor_notes
        self.roast_date = roast_date

    @staticmethod
    def from_dict(source):
        # Initialize CoffeeBeans class
        coffee_beans = CoffeeBeans(source[CoffeeBeans.PRODUCER], source[CoffeeBeans.COUNTRY_OF_ORIGIN])
        # Delete used fields from source dictionary
        del source[CoffeeBeans.PRODUCER]
        del source[CoffeeBeans.COUNTRY_OF_ORIGIN]

        # Set remaining attributes in source dictionary to class
        for key in source:
            setattr(coffee_beans, key, source[key])
        return coffee_beans

    def to_dict(self):
        return dict((key, value) for (key, value) in self.__dict__.items())