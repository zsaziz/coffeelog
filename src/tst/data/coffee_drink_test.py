# local lib
from data.coffee_drink import CoffeeDrink
from data.coffee_beans import CoffeeBeans
from exceptions.missing_argument_error import MissingArgumentError
from utils.common_utils import get_current_local_datetime

from tst.data.coffee_base_test import CoffeeBaseTest

# python lib
import unittest

class CoffeeDrinkTest(CoffeeBaseTest):
    
    def test_coffee_drink_init(self):
        cd1 = CoffeeDrink('drink1', 1)
    
    def test_coffee_drink_init_exception(self):
        with self.assertRaises(MissingArgumentError):
            cd_fail = CoffeeDrink('drink', None)
        with self.assertRaises(MissingArgumentError):
            cd_fail = CoffeeDrink(None, 1)

    def test_coffee_drink_to_dict(self):
        roast_date = get_current_local_datetime().date
        cb = CoffeeBeans('producer', 'country', 'beans_name', 5, ['note1', 'note2'], roast_date)

        cd_all_attributes = CoffeeDrink(
            'drink_all',
            10,
            'milk_test',
            ['add1', 'add2'],
            cb,
            'cafe_test'
        )

        entry_datetime = get_current_local_datetime()
        actual_dict = cd_all_attributes.to_dict()
        actual_dict[CoffeeDrink.ENTRY_DATETIME] = entry_datetime

        expected_dict = {
            'cafe': 'cafe_test',
            'quantity_in_fluid_oz': 10,
            'drink': 'drink_all',
            'additives': ['add1', 'add2'],
            'milk_options': 'milk_test',
            'entry_datetime': entry_datetime,
            'coffee_beans': {
                'producer': 'producer',
                'roast_date': roast_date,
                'country_of_origin': 'country',
                'roast_level': 5,
                'flavor_notes': ['note1', 'note2'],
                'name': 'beans_name'
                }
            }
        
        self.assertEqual(actual_dict, expected_dict)

    def test_coffee_drink_from_dict(self):
        roast_date = get_current_local_datetime().date

        source_dict = {
            'cafe': 'cafe_test',
            'quantity_in_fluid_oz': 10,
            'drink': 'drink_all',
            'additives': ['add1', 'add2'],
            'milk_options': 'milk_test',
            'entry_datetime': None,
            'coffee_beans': {
                'producer': 'producer',
                'roast_date': roast_date,
                'country_of_origin': 'country',
                'roast_level': 5,
                'flavor_notes': ['note1', 'note2'],
                'name': 'beans_name'
                }
            }

        cb = CoffeeBeans('producer', 'country', 'beans_name', 5, ['note1', 'note2'], roast_date)
        expected_cd = CoffeeDrink(
            'drink_all',
            10,
            'milk_test',
            ['add1', 'add2'],
            cb,
            'cafe_test'
        )
        expected_cd.entry_datetime = None

        actual = CoffeeDrink.from_dict(source_dict)
        self.assertEqual(str(actual), str(expected_cd))
