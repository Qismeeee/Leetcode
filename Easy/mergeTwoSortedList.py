class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
        

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)) if result else "None")


# Test cases
solution = Solution()
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
print("Test case 1:")
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)

# Test case 2
list1 = create_linked_list([1, 3, 5])
list2 = create_linked_list([])
print("Test case 2 (list2 is empty):")
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)

list1 = create_linked_list([])
list2 = create_linked_list([2, 4, 6])
print("Test case 2 (list1 is empty):")
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)

# Test case 3
list1 = create_linked_list([])
list2 = create_linked_list([])
print("Test case 3 (both lists are empty):")
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)

# Test case 4
list1 = create_linked_list([1, 3, 5])
list2 = create_linked_list([2, 4])
print("Test case 4 (lists of different lengths):")
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)

# Test case 5
list1 = create_linked_list([1, 1, 1])
list2 = create_linked_list([1, 1, 1])
print("Test case 5 (identical values):")
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)
