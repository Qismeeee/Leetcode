class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)

# Test case
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(50)

stack.display()

print("Peek: ", stack.peek())
print("Pop: ", stack.pop())
stack.display()
print("Size: ", stack.size())