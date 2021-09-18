class NonPositiveError(Exception):
    def __init__(self):
        pass


class PositiveList(list):
    def __init__(self, value=[]):
        super().__init__([])
        for item in value:
            self.append(item)

    def append(self, value):
        if value <= 0:
            raise NonPositiveError
        else:
            super().append(value)
