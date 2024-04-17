# 3P lib
from google.cloud import firestore

# local lib
from data.coffee_drink import CoffeeDrink
from data.coffee_beans import CoffeeBeans
from utils.common_utils import yes_or_no
from utils.logging_utils import get_logger

# python lib
import time

log = get_logger(__name__)

DEFAULT_DATABASE = 'coffeelog-metadata'
COFFEE_DRINK_COLLECTION = CoffeeDrink.COFFEE_DRINK_NAME
COFFEE_BEANS_COLLECTION = CoffeeBeans.COFFEE_BEANS_NAME
BATCH_SIZE = 10

class FirestoreClient:
    def __init__(self):
        self.creds_path = 'creds/google/coffeelog_service_account_creds.json'
        self.db = firestore.Client().from_service_account_json(self.creds_path, database='coffeelog-metadata')

    # CoffeeDrink APIs

    def create_coffee_drink(self, coffee_drink: CoffeeDrink):
        doc_ref = self.db.collection(COFFEE_DRINK_COLLECTION).document()
        doc_ref.set(coffee_drink.to_dict())
        return doc_ref.id

    def delete_coffee_drink(self, doc_id: str):
        self.db.collection(COFFEE_DRINK_COLLECTION).document(doc_id).delete()

    def delete_coffee_drink_collection(self):
        """WARNING! This method will delete the entire CoffeeDrink collection, including ALL documents present.
        
        Proceed with caution.
        """

        # User input verification
        yes_or_no(self._get_del_col_warning_message(COFFEE_DRINK_COLLECTION))
        
        self._delete_collection_recursive(COFFEE_DRINK_COLLECTION,
            list(self.db.collection(COFFEE_DRINK_COLLECTION).list_documents(page_size=BATCH_SIZE)))
        log.info(f'Successfully deleted collection {COFFEE_DRINK_COLLECTION}')

    # Common functionalities
 
    # Recursively delete all documents in collection by batch size  
    def _delete_collection_recursive(self, collection, doc_list):
        if not doc_list:
            return
        
        for doc in doc_list:
            log.info(f'Deleting doc {doc.id} => {doc.get().to_dict()}...')
            doc.delete()
            log.info(f'Deleted doc {doc.id}')

        time.sleep(0.5)
        return self._delete_collection_recursive(collection,
            list(self.db.collection(collection).list_documents(page_size=BATCH_SIZE))
        )

    def _get_del_col_warning_message(self, resource_name):
        return f'This method will delete the entire {resource_name} collection, including ALL documents present.'