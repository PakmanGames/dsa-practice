class StackList:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) <= 0

    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return f"{self.stack}"

stack1 = StackList()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1)
stack1.pop()
print(stack1)