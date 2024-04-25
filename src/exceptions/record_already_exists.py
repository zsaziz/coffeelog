class RecordAlreadyExists(Exception):
    """Exception raised when a required argument is missing.
    """

    def __init__(self, record_id):
        self.message = f'Record {record_id} already exists.'
        super().__init__(self.message)
