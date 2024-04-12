from clients.google.google_client import GoogleClient

if __name__ == "__main__":
    db = GoogleClient().firestore_client()

    data = {
        "Drink": ""
    }
    db.collection('CoffeeInfo').document()