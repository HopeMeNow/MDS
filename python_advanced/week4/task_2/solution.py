class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.buffer = []

    def add(self, *a):
        for elem in a:
            self.buffer.append(elem)
            if len(self.buffer) == self.maxsize:
                print(sum(self.buffer))
                self.buffer.clear()

    def get_current_part(self):
        return self.buffer
