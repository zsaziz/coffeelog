# local lib
from data.coffee_beans import CoffeeBeans
from exceptions.missing_argument_error import MissingArgumentError
from utils.common_utils import get_current_local_datetime

from tst.data.coffee_base_test import CoffeeBaseTest

# python lib
import unittest

class CoffeeBeansTest(CoffeeBaseTest):

    def test_coffee_beans_init(self):
        cb = CoffeeBeans('producer', 'country')

    def test_coffee_beans_init_exception(self):
        with self.assertRaises(MissingArgumentError):
            CoffeeBeans('producer', None)
        with self.assertRaises(MissingArgumentError):
            CoffeeBeans(None, 'country')
        with self.assertRaises(ValueError):
            # Roast level out of range
            CoffeeBeans('prod', 'country', roast_level=11)
    
    def test_coffee_beans_to_dict(self):
        roast_date = get_current_local_datetime().date
        cb = CoffeeBeans('producer', 'country', 'beans_name', 5, ['note1', 'note2'], roast_date)
        actual = cb.to_dict()

        expected = {
            'producer': 'producer',
            'roast_date': roast_date,
            'country_of_origin': 'country',
            'roast_level': 5,
            'flavor_notes': ['note1', 'note2'],
            'name': 'beans_name'
        }

        self.assertEqual(actual, expected)

    def test_coffee_beans_from_dict(self):
        roast_date = get_current_local_datetime().date

        actual = CoffeeBeans.from_dict({
            'producer': 'producer',
            'roast_date': roast_date,
            'country_of_origin': 'country',
            'roast_level': 5,
            'flavor_notes': ['note1', 'note2'],
            'name': 'beans_name'
        })

        expected = CoffeeBeans('producer', 'country', 'beans_name', 5, ['note1', 'note2'], roast_date)

        self.assertEqual(str(actual), str(expected))
