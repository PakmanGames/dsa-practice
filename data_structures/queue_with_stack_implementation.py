class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) <= 0

    def __str__(self):
        return f"{self.stack}"

class Queue:
    def __init__(self):
        self.stack = StackList()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        temp_stack = StackList()
        while not self.stack.isEmpty():
            temp_stack.push(self.stack.pop())
        res = temp_stack.pop()
        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())
        return res

    def __str__(self):
        return f"{self.stack}"

queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
print(queue1)
queue1.dequeue()
print(queue1)