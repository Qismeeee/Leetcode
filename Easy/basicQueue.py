class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    def display(self):
        print(self.queue)

# Test cases:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(100)
queue.display()

print("Front: ", queue.front())
print("Dequeue: ", queue.dequeue())
queue.display()
print("Size: ", queue.size())