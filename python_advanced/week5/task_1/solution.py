class FlashError(Exception):
    def __init__(self):
        pass


class FlashMaxFileSizeError(FlashError):
    def __init__(self):
        pass


class FlashMemoryLimitError(FlashError):
    def __init__(self):
        pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.max_file_size = max_file_size

    def write(self, v):
        if self.max_file_size is not None and v > self.max_file_size:
            raise FlashMaxFileSizeError
        elif self.capacity < v:
            raise FlashMemoryLimitError
        else:
            self.capacity -= v
