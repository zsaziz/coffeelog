class MissingArgumentError(Exception):
    """Exception raised when a required argument is missing.
    """

    def __init__(self, attribute_name):
        self.message = f'{attribute_name} is required but missing.'
        super().__init__(self.message)