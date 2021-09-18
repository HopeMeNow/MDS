class Flash:
    def __init__(self, capacity):
        self.capacity = capacity

    def write(self, filesize):
        if (self.capacity - filesize) < 0:
            raise ValueError("Insufficient disk space")
        else:
            self.capacity = self.capacity - filesize
