class WordNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class BadInput(Exception):
    def __init__(self, message):
        super().__init__(message)
