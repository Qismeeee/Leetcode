class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        current_idx = 0
        current_node = self.head
        while current_node.next != None and current_idx < index:
            current_node = current_node.next
            current_idx += 1
        return current_node.data

    def remove(self, index):
        if index >= self.length():
            print("Index out of range")
            return
        current_idx = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next
            if current_idx == index:
                last_node.next = current_node.next
                return
            current_idx += 1


my_list = linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print(f"Length of the list: {my_list.length()}")
my_list.display()
value = my_list.get(2)
print(f"Element at 2nd index: {value}")
rm_value = my_list.remove(1)
my_list.display()
