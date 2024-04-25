from tst.data.coffee_drink_test import CoffeeDrinkTest
from tst.data.coffee_beans_test import CoffeeBeansTest

def data_tests():
    CoffeeDrinkTest().run_tests()
    CoffeeBeansTest().run_tests()

if __name__ == "__main__":
    data_tests()
