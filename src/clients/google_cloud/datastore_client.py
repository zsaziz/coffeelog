# 3P lib
from google.cloud import datastore
from google.cloud.datastore.query import PropertyFilter

# local lib
from data.coffee_drink import CoffeeDrink
from data.coffee_beans import CoffeeBeans
from data.update_coffee_drink import UpdateCoffeeDrink
from exceptions.record_already_exists import RecordAlreadyExists
from utils.common_utils import yes_or_no
from utils.logging_utils import get_logger

# python lib
import time
from typing import List

log = get_logger(__name__)

DEFAULT_DATABASE = 'coffeelog-data'
BATCH_SIZE = 20

class DatastoreClient:
    def __init__(self):
        self.creds_path = 'creds/google/coffeelog_service_account_creds.json'
        self.client = datastore.Client().from_service_account_json(self.creds_path, database=DEFAULT_DATABASE)

    # CoffeeDrink APIs

    def create_coffee_drink(self, coffee_drink: CoffeeDrink):
        with self.client.transaction():
            key = self.client.key(CoffeeDrink.COFFEE_DRINK_NAME, coffee_drink.brew_id)
            entity = self.client.get(key)

            if entity:
                raise RecordAlreadyExists(coffee_drink.brew_id)
            
            entity = datastore.Entity(key)
            entity.update(coffee_drink.to_dict())
            self.client.put(entity)

        log.info(f'Created record {coffee_drink.brew_id}')

    def get_coffee_drink(self, brew_id: str):
        entity = self.client.get(self.client.key(CoffeeDrink.COFFEE_DRINK_NAME, brew_id))
        return self._entity_to_coffee_drink_mapper(entity)

    def list_coffee_drinks(self, user_id: str):
        """Returns list of entities for user
        """
        return self.list_coffee_drinks_with_filters(
            PropertyFilter(CoffeeDrink.USER_ID, '=', user_id)
        )

    def list_coffee_drinks_with_filters(self, *filters: PropertyFilter):
        query = self.client.query(kind=CoffeeDrink.COFFEE_DRINK_NAME)
        for filt in filters:
            query.add_filter(filter=filt)
        return [self._entity_to_coffee_drink_mapper(entity) for entity in list(query.fetch())]

    def update_coffee_drink(self, brew_id: str, update_coffee_drink: UpdateCoffeeDrink):
        entity = self.client.get(self.client.key(CoffeeDrink.COFFEE_DRINK_NAME, brew_id))
        for key, val in update_coffee_drink.to_dict().items():
            if val:
                entity[key] = val
        self.client.put(entity)


    def delete_coffee_drink(self, brew_id: str):
        self.client.delete(self.client.key(CoffeeDrink.COFFEE_DRINK_NAME, brew_id))
        log.info(f'Deleted record {brew_id}')

    def _delete_all_coffee_drinks(self):
        """WARNING! This method will delete all entities of CoffeeDrink kind.
        
        Proceed with caution.
        """

        # User input verification
        yes_or_no(self._get_del_col_warning_message(CoffeeDrink.COFFEE_DRINK_NAME))

        query = self.client.query(kind=CoffeeDrink.COFFEE_DRINK_NAME)
        entities = list(query.fetch(limit=BATCH_SIZE))
        while entities:
            for entity in entities:
                self.client.delete(entity.key)
            entities = list(query.fetch(limit=BATCH_SIZE))
            time.sleep(0.5)
        log.info('Deleted all entities')

    def _get_del_col_warning_message(self, kind_name):
        return f'This method will delete all entities of kind {kind_name}'
    
    def _entity_to_coffee_drink_mapper(self, entity):
        return CoffeeDrink.from_dict(dict(entity.items()))