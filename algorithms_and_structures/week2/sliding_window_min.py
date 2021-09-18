class Stack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        return self.stack.append(key)

    def pop(self):
        return self.stack.pop()

    def bottom(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()

    def top(self):
        if self.empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, key):
        cur_min = self.min_stack.top() if not self.min_stack.empty() else key
        self.min_stack.push(min(cur_min, key))
        return self.stack.push(key)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def bottom(self):
        return self.stack.bottom()

    def empty(self):
        return self.stack.empty()

    def clear(self):
        self.stack.clear()

    def top(self):
        return self.stack.top()

    def size(self):
        return self.stack.size()

    def min(self):
        return self.min_stack.top()


class Queue:
    def __init__(self):
        self.to_enqueue = MinStack()
        self.to_dequeue = MinStack()

    def push(self, key):
        return self.to_enqueue.push(key)

    def pop(self):
        if self.empty():
            return 'error'
        else:
            if self.to_dequeue.empty():
                while not self.to_enqueue.empty():
                    self.to_dequeue.push(self.to_enqueue.pop())
            return self.to_dequeue.pop()

    def top(self):
        if self.empty():
            return 'error'
        else:
            if not self.to_dequeue.empty():
                return self.to_dequeue.top()
            else:
                return self.to_enqueue.stack.bottom()

    def empty(self):
        return self.to_dequeue.empty() and self.to_enqueue.empty()

    def clear(self):
        self.to_enqueue.clear()
        self.to_dequeue.clear()

    def size(self):
        return self.to_enqueue.size() + self.to_dequeue.size()

    def min(self):
        if self.to_enqueue.empty() and self.to_dequeue.empty():
            return None
        if self.to_dequeue.empty():
            return self.to_enqueue.min()
        if self.to_enqueue.empty():
            return self.to_dequeue.min()

        return min(self.to_enqueue.min(), self.to_dequeue.min())


def sliding_window_min(a, k):
    mins = []
    queue = Queue()

    for i in range(len(a)):
        queue.push(a[i])

        if i >= k:
            queue.pop()

        if i >= k-1:
            mins.append(queue.min())

    return mins


# some test code
if __name__ == "__main__":
    test_a, test_k = [1, 3, 4, 5, 2, 7], 3


    # should print [1, 3, 2, 2]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [5, 4, 10, 1], 2
    # should print [4, 4, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [10, 20, 6, 10, 8], 5
    # should print [6]
    print(sliding_window_min(test_a, test_k))
