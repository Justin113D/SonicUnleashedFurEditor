
class SUFEException(Exception):

    message: str

    def __init__(self, message: str, *args: object):
        self.message = message
        super().__init__(message, *args)


class SUFEDevException(SUFEException):

    def __init__(self, message: str, *args: object):
        super().__init__("Developer error, please report:\n" + message, *args)


class SUFEUserException(SUFEException):

    def __init__(self, message: str, *args: object):
        super().__init__(message, *args)
