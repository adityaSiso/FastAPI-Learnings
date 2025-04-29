class CustomException(Exception):
    def __init__(self, detail, *args):
        self.detail = detail
        super().__init__(*args)