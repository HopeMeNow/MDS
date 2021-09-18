class Queue:
    def __init__(self):
        self.input_list = []
        self.output_list = []

    def push(self, x):
        self.input_list.append(x)
        self.output_list = self.input_list[::-1]

    def pop(self):
        if len(self.output_list) == 0:
            raise IndexError('pop from an empty queue')
        else:
            pop_value = self.output_list.pop()
            self.input_list = self.output_list[::-1]
            return pop_value
