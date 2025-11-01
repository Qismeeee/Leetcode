class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        ban = set(nums)
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur:
            if cur.val in ban:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next
