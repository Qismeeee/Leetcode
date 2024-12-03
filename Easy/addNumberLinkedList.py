class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(10)
print(node.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

ll = LinkedList()

ll.append(10)
ll.append(20)

current = ll.head
while current:
    print(current.data)
    current = current.next