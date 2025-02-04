class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return f"{self.queue}"

queue1 = QueueList()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)

print(queue1)
queue1.dequeue()
print(queue1)