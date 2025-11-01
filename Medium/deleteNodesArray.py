class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

s = Solution()

nums = [1,2,3]; head = build_list([1,2,3,4,5])
print(to_list(s.modifiedList(nums, head)))  # [4, 5]

nums = [1]; head = build_list([1,2,1,2,1,2])
print(to_list(s.modifiedList(nums, head)))  # [2, 2, 2]

nums = [5]; head = build_list([1,2,3,4])
print(to_list(s.modifiedList(nums, head)))  # [1, 2, 3, 4]
