

class AppException(Exception):
    def to_dict(self):
        rv = self.payload or {}
        rv['message'] = self.message
        return rv


class InvalidLoginCredentialsException(AppException):
    status_code = 400

    def __init__(self, message, payload=None):
        AppException.__init__(self)
        self.message = message
        self.payload = payload


class MissingCredentialsException(AppException):
    status_code = 400

    def __init__(self, message, payload=None):
        AppException.__init__(self)
        self.message = message
        self.payload = payload
