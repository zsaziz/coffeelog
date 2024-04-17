# local lib
from data.coffee_beans import CoffeeBeans
from data.coffee_drink import CoffeeDrink
from clients.google_cloud.firestore_client import FirestoreClient


def generate_coffee_drinks(firestore_client: FirestoreClient, range_val, beans):
    if beans:
        for i in range_val:
            firestore_client.create_coffee_drink(CoffeeDrink(f'drink{i}', i+10, coffee_beans=CoffeeBeans(f'beans{i}', f'country{i}')))
    else:
        for i in range_val:
            firestore_client.create_coffee_drink(CoffeeDrink(f'drink{i}', i+10))


if __name__ == "__main__":
    # firestore = FirestoreClient()
    # generate_coffee_drinks(firestore, range(0,10), False)
    # generate_coffee_drinks(firestore, range(10,20), True)

    # firestore.delete_coffee_drink('zDM4DvK5DL0TxPGwdgKB')
    # firestore.delete_coffee_drink_collection()