class Stack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        return self.stack.append(key)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class Deque:
    def __init__(self):
        self.to_enqueue = Stack()
        self.to_dequeue = Stack()

    def push_front(self, key):
        self.to_dequeue.push(key)
        return 'ok'

    def push_back(self, key):
        self.to_enqueue.push(key)
        return 'ok'

    def pop_front(self):
        if self.empty():
            return 'error'
        else:
            if self.to_dequeue.empty():
                while not self.to_enqueue.empty():
                    self.to_dequeue.push(self.to_enqueue.pop())
            return self.to_dequeue.pop()

    def pop_back(self):
        if self.empty():
            return 'error'
        else:
            if self.to_enqueue.empty():
                while not self.to_dequeue.empty():
                    self.to_enqueue.push(self.to_dequeue.pop())
            return self.to_enqueue.pop()

    def front(self):
        if self.empty():
            return 'error'
        else:
            if not self.to_dequeue.empty():
                return self.to_dequeue.top()
            else:
                return self.to_enqueue.stack[0]

    def back(self):
        if self.empty():
            return 'error'
        else:
            if not self.to_enqueue.empty():
                return self.to_enqueue.top()
            else:
                return self.to_dequeue.stack[0]

    def empty(self):
        return self.to_dequeue.empty() and self.to_enqueue.empty()

    def clear(self):
        self.to_enqueue.clear()
        self.to_dequeue.clear()
        return 'ok'

    def size(self):
        return self.to_enqueue.size() + self.to_dequeue.size()

    def __str__(self):
        en = self.to_enqueue.stack
        de = list(reversed(self.to_dequeue.stack))
        return str(de + en)


def process_deque(commands):
    deque = Deque()

    queue_methods = {
        'push_front': deque.push_front,
        'push_back': deque.push_back,
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
        'front': deque.front,
        'back': deque.back,
        'clear': deque.clear,
        'size': deque.size,
    }

    res = []
    for command in commands:
        method_and_arg = command.split(' ')

        if len(method_and_arg) > 1:
            res.append(queue_methods[method_and_arg[0]](int(method_and_arg[1])))
        else:
            res.append(queue_methods[method_and_arg[0]]())
    return res


if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))