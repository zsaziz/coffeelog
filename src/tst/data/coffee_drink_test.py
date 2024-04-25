# local lib
from data.coffee_drink import CoffeeDrink
from data.coffee_beans import CoffeeBeans
from exceptions.missing_argument_error import MissingArgumentError
from utils.common_utils import get_current_local_datetime

from tst.data.coffee_base_test import CoffeeBaseTest

# python lib
import unittest

TEST_USER = 'test-user'

class CoffeeDrinkTest(CoffeeBaseTest):
    def setUp(self):
        self.maxDiff = None
    
    def test_coffee_drink_init(self):
        cd1 = CoffeeDrink(TEST_USER,TEST_USER, 'drink1', 1)
    
    def test_coffee_drink_init_exception(self):
        with self.assertRaises(MissingArgumentError):
            cd_fail = CoffeeDrink(None,'drink', None)
        with self.assertRaises(MissingArgumentError):
            cd_fail = CoffeeDrink(TEST_USER,'drink', None)
        with self.assertRaises(MissingArgumentError):
            cd_fail = CoffeeDrink(TEST_USER, None, 1)

    def test_coffee_drink_to_dict(self):
        roast_date = get_current_local_datetime().date
        cb = CoffeeBeans('producer', 'country', 'beans_name', 5, ['note1', 'note2'], roast_date)

        cd_all_attributes = CoffeeDrink(
            TEST_USER,
            drink='drink_all',
            quantity_in_fl_oz=10,
            milk_options='milk_test',
            additives=['add1', 'add2'],
            coffee_beans=cb,
            cafe='cafe_test'
        )

        actual_dict = cd_all_attributes.to_dict()

        expected_dict = {
            'cafe': 'cafe_test',
            'quantity_in_fl_oz': 10,
            'drink': 'drink_all',
            'additives': ['add1', 'add2'],
            'milk_options': 'milk_test',
            'entry_datetime': actual_dict[CoffeeDrink.ENTRY_DATETIME],
            'user_id': TEST_USER,
            'brew_id': f'{TEST_USER}-drink_all-{int(actual_dict[CoffeeDrink.ENTRY_DATETIME].timestamp())}',
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
            'quantity_in_fl_oz': 10,
            'drink': 'drink_all',
            'additives': ['add1', 'add2'],
            'milk_options': 'milk_test',
            'entry_datetime': None,
            'user_id': TEST_USER,
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
            TEST_USER,
            'drink_all',
            10,
            'milk_test',
            ['add1', 'add2'],
            cb,
            'cafe_test'
        )

        source_dict[CoffeeDrink.ENTRY_DATETIME] = expected_cd.entry_datetime
        source_dict[CoffeeDrink.BREW_ID] = f'{TEST_USER}-drink_all-{int(expected_cd.entry_datetime.timestamp())}'

        actual = CoffeeDrink.from_dict(source_dict)
        self.assertEqual(str(actual), str(expected_cd))
