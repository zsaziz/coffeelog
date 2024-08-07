class NotAuthenticatedError(Exception):
    """Exception raised if user is not authenticated on a protected route.
    """

    def __init__(self):
        self.message = 'You must be logged in to access this page'
        super().__init__(self.message)
