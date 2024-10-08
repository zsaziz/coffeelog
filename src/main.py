# USED FOR TESTING DURING DEVELOPMENT
# DO NOT EXPOSE IN PROD

# local lib
import sys
from data.coffee_beans import CoffeeBeans
from data.update_coffee_drink import UpdateCoffeeDrink
from data.coffee_drink import CoffeeDrink
from clients.google_cloud.datastore_client import DatastoreClient

# Flask app
from app import main

user = 'zoon'

if __name__ == "__main__":
    main()
    sys.exit()

    datastore = DatastoreClient()

    # coffee = CoffeeDrink(user, 'drip', 12)
    # datastore.create_coffee_drink(coffee)

    coffee = datastore.get_coffee_drink('zoon-drip-1713908920')
    print(coffee)
    update_coffee = UpdateCoffeeDrink(quantity_in_fl_oz=16)
    datastore.update_coffee_drink(coffee.brew_id, update_coffee)
    update_coffee = datastore.get_coffee_drink('zoon-drip-1713908920')
    print(update_coffee)


    # coffee_b = CoffeeDrink('test', 'drip', 12, additives=['cardammom', 'rose'], coffee_beans=CoffeeBeans('Cafe Vita', 'Guatamala'))
    # entity = datastore.get_coffee_drink('test-drip-1713676592')

    # generate_coffee_drinks(datastore, range(0,10))
    # datastore._delete_all_coffee_drinks()

    # filt = PropertyFilter('user_id', '>', 'zoon')
    # drinks = datastore.list_coffee_drinks('zoon0')
    # for x in drinks:
    #     print(x)
    # exit()

    # coffee = CoffeeDrink(user, 'espresso', 6)
    # coffee.brew_id = 'zoon-drip-1713675633'
    # datastore.create_coffee_drink(coffee)

    # coffee_b = CoffeeDrink(user, 'drip', 12, coffee_beans=CoffeeBeans('Cafe Vita', 'Guatamala'))
    # datastore.create_coffee_drink(coffee_b)
    # generate_coffee_drinks(firestore, range(0,5), True)
    # generate_coffee_drinks(firestore, range(10,20), True)

    # field_path = FieldPath(CoffeeBeans.COFFEE_BEANS_NAME, CoffeeBeans.ROAST_LEVEL)
    # filt1 = FieldFilter('coffee_beans.roast_level', '>=', 5)
    # filt2 = FieldFilter('coffee_drink', '==', 'zoon3')
    # # filt2 = FieldFilter('drink', '<', 'oon' + 'z')
    # for x in firestore.get_coffee_drink_query(filt1, filt2):
    #     print(x)

    # x = firestore.get_coffee_drink_with_id('3lXeglNaGjJA6YJDUVi9')
    # print(x)
    # date = x.entry_datetime
    # localized = datetime.fromtimestamp(int(date.timestamp()), date.tzinfo).astimezone().replace(microsecond=0)
    # print(localized, type(localized), localized.tzinfo)

    # firestore.delete_coffee_drink('zDM4DvK5DL0TxPGwdgKB')
    # firestore.delete_coffee_drink_collection()
