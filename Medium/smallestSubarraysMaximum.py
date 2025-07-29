class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n
        rightmost_bit_pos = [-1] * 32  
        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    rightmost_bit_pos[bit] = i
            
            max_or = 0
            furthest_needed = i  
            for bit in range(32):
                if rightmost_bit_pos[bit] >= i: 
                    max_or |= (1 << bit)
                    furthest_needed = max(furthest_needed, rightmost_bit_pos[bit])
            
            answer[i] = furthest_needed - i + 1
        
        return answer
    
def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1, 0, 2, 1, 3]
    result1 = sol.smallestSubarrays(nums1)
    print(f"Example 1: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [3, 3, 2, 2, 1]")
    print()
    print("Tracing Example 1:")
    for i in range(len(nums1)):
        print(f"Starting at index {i} (value {nums1[i]}):")
        current_or = 0
        for j in range(i, len(nums1)):
            current_or |= nums1[j]
            print(f"  Subarray [{i}:{j+1}] = {nums1[i:j+1]} -> OR = {current_or}")
        print(f"  Max OR from position {i}: {current_or}")
        print(f"  Shortest length: {result1[i]}")
        print()
    
    # Example 2
    nums2 = [1, 2]
    result2 = sol.smallestSubarrays(nums2)
    print(f"Example 2: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [2, 1]")
    print()
    
    nums3 = [1, 2, 4]
    result3 = sol.smallestSubarrays(nums3)
    print(f"Test 3: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [3, 2, 1]")
    print()

test_solution()