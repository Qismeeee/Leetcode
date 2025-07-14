
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        result = 0
        current = head
        while current:
            result = result * 2 + current.val
            current = current.next
        
        return result

def test_solution():
    sol = Solution()
    
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head
    
    def print_linked_list(head):
        values = []
        current = head
        while current:
            values.append(str(current.val))
            current = current.next
        return "[" + ",".join(values) + "]"
    
    head1 = create_linked_list([1, 0, 1])
    result1 = sol.getDecimalValue(head1)
    print(f"Example 1: {print_linked_list(head1)} -> {result1}") 
    head2 = create_linked_list([0])
    result2 = sol.getDecimalValue(head2)
    print(f"Example 2: {print_linked_list(head2)} -> {result2}") 
    print(f"\nTracing Example 1: [1,0,1]")
    print(f"Binary: 101₂")
    print(f"Step 1: result = 0*2 + 1 = 1")
    print(f"Step 2: result = 1*2 + 0 = 2") 
    print(f"Step 3: result = 2*2 + 1 = 5")
    print(f"Final: 5₁₀")
    
    print(f"\nAdditional tests:")
    # [1] -> 1
    head3 = create_linked_list([1])
    result3 = sol.getDecimalValue(head3)
    print(f"[1] -> {result3}")
    
    # [1,0,0,1] -> 9
    head4 = create_linked_list([1, 0, 0, 1])
    result4 = sol.getDecimalValue(head4)
    print(f"[1,0,0,1] -> {result4}")
    
    # [1,1,1] -> 7  
    head5 = create_linked_list([1, 1, 1])
    result5 = sol.getDecimalValue(head5)
    print(f"[1,1,1] -> {result5}")
    
    print(f"\nVerification:")
    print(f"101₂ = 1×2² + 0×2¹ + 1×2⁰ = 4 + 0 + 1 = 5 ✓")
    print(f"1001₂ = 1×2³ + 0×2² + 0×2¹ + 1×2⁰ = 8 + 0 + 0 + 1 = 9 ✓")
    print(f"111₂ = 1×2² + 1×2¹ + 1×2⁰ = 4 + 2 + 1 = 7 ✓")

test_solution()