class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next

        middle_node = count // 2
        current_node = head
        for _ in range(middle_node):
            current_node = current_node.next
        return current_node

    def display(self, head):
        middle_node = self.middleNode(head)
        current_node = middle_node
        elements = []
        while current_node:
            elements.append(current_node.val)
            current_node = current_node.next
        print(elements)

    def create_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print_linked_list(self, head):
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        print(" -> ".join(map(str, elements)) if elements else "Empty list")


solution = Solution()

# Test case 1
head = solution.create_linked_list([1, 2, 3, 4, 5])
print("Input List:")
solution.print_linked_list(head)
middle = solution.middleNode(head)
print("Middle Node Value:", middle.val)
print(solution.display(head))

# Test case 2
head = solution.create_linked_list([1, 2, 3, 4, 5, 6])
print("\nInput List:")
solution.print_linked_list(head)
middle = solution.middleNode(head)
print("Middle Node Value:", middle.val)
