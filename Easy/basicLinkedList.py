# Linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# a = node(1)
# b = node(4)
# c = node(5)

# a.next = b
# b.next = c

# print(a.next.next.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def remove(self, data):
        if self.head is None:
            print("Danh sách rỗng.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is None:
            print("Không tìm thấy giá trị", data)
        else:
            current_node.next = current_node.next.next

    def get(self, index):
        if index < 0:
            return None
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node.data
            current_node = current_node.next
            count += 1
        return None

    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count


list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.append(8)
list1.append(10)
list1.display()

list1.remove(8)
list1.display()

print(list1.get(1))
print(list1.length())
