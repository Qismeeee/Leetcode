class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        i = 1  
        while i < n - 1:  
            left_neighbor = None
            for j in range(i - 1, -1, -1):
                if nums[j] != nums[i]:
                    left_neighbor = nums[j]
                    break
            right_neighbor = None
            for j in range(i + 1, n):
                if nums[j] != nums[i]:
                    right_neighbor = nums[j]
                    break
            
            if left_neighbor is not None and right_neighbor is not None:
                current = nums[i]
                if current > left_neighbor and current > right_neighbor:
                    count += 1
                    while i + 1 < n and nums[i + 1] == current:
                        i += 1
                
                elif current < left_neighbor and current < right_neighbor:
                    count += 1
                    while i + 1 < n and nums[i + 1] == current:
                        i += 1
            
            i += 1
        
        return count
    
def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [2,4,1,1,6,5]
    result1 = sol.countHillValley(nums1)
    print(f"Example 1: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 3")
    print()
    
    # Example 2
    nums2 = [6,6,5,5,4,1]
    result2 = sol.countHillValley(nums2)
    print(f"Example 2: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 0")
    print()
    
    nums3 = [2,1,2]
    result3 = sol.countHillValley(nums3)
    print(f"Test 3: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 1 (valley at index 1)")
    print()
    
    nums4 = [1,2,1]
    result4 = sol.countHillValley(nums4)
    print(f"Test 4: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: 1 (hill at index 1)")
    print()

test_solution()