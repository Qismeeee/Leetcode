class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_count = sum(1 for x in nums if x % 2 == 0)
        odd_count = len(nums) - even_count

        max_length = max(even_count, odd_count)
        length = 0
        need_even = True
        for num in nums:
            if (num % 2 == 0) == need_even:
                length += 1
                need_even = not need_even
        max_length = max(max_length, length)
        length = 0
        need_odd = True
        for num in nums:
            if (num % 2 == 1) == need_odd:
                length += 1
                need_odd = not need_odd
        max_length = max(max_length, length)
        
        return max_length
    
def test_solution():
    sol = Solution()
    
    result1 = sol.maximumLength([1,2,3,4])
    print(f"Example 1: {result1}")  
    result2 = sol.maximumLength([1,2,1,1,2,1,2])
    print(f"Example 2: {result2}")  
    result3 = sol.maximumLength([1,3])
    print(f"Example 3: {result3}")  
    nums1 = [1,2,3,4]
    print(f"\nTracing Example 1: {nums1}")
    
    even_count = sum(1 for x in nums1 if x % 2 == 0)
    odd_count = len(nums1) - even_count
    print(f"Even count: {even_count}, Odd count: {odd_count}")
    
    print(f"Pattern 3 (start even):")
    length = 0
    need_even = True
    for i, num in enumerate(nums1):
        if (num % 2 == 0) == need_even:
            print(f"  Take {num} at index {i} (length = {length + 1})")
            length += 1
            need_even = not need_even
        else:
            print(f"  Skip {num} at index {i} (need {'even' if need_even else 'odd'})")
    print(f"  Final length: {length}")
    
    print(f"Pattern 4 (start odd):")
    length = 0
    need_odd = True
    for i, num in enumerate(nums1):
        if (num % 2 == 1) == need_odd:
            print(f"  Take {num} at index {i} (length = {length + 1})")
            length += 1
            need_odd = not need_odd
        else:
            print(f"  Skip {num} at index {i} (need {'odd' if need_odd else 'even'})")
    print(f"  Final length: {length}")
    
    subseq = [1,2,3,4]
    print(f"\nVerifying subsequence {subseq}:")
    for i in range(len(subseq) - 1):
        parity = (subseq[i] + subseq[i+1]) % 2
        print(f"  ({subseq[i]} + {subseq[i+1]}) % 2 = {parity}")
    
    print(f"\nAdditional tests:")
    print(f"All even [2,4,6,8]: {sol.maximumLength([2,4,6,8])}")  # 4
    print(f"All odd [1,3,5,7]: {sol.maximumLength([1,3,5,7])}")    # 4
    print(f"Mixed [1,1,2,2]: {sol.maximumLength([1,1,2,2])}")      # 3

test_solution()