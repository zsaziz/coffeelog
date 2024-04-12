from google.cloud import firestore

class GoogleClient:
    def __init__(self):
        self.creds_path = 'src/creds/google/coffeelog_service_account_creds.json'
        self.default_database = 'coffeelog-metadata'

    def firestore_client(self, database=''):
        return firestore.Client(database=f'{database if database else self.default_database}').from_service_account_json(self.creds_path)
