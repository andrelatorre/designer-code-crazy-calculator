class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEmtity'
        self.status_code = 422