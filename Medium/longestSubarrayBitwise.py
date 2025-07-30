class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        max_length = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
        
        return max_length
    
def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 3, 2, 2]
    result1 = sol.longestSubarray(nums1)
    print(f"Example 1: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print(f"Max value: {max(nums1)}")
    print(f"Longest consecutive sequence of max value: [3,3]")
    print()
    
    # Example 2
    nums2 = [1, 2, 3, 4]
    result2 = sol.longestSubarray(nums2)
    print(f"Example 2: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print(f"Max value: {max(nums2)}")
    print(f"Longest consecutive sequence of max value: [4]")
    print()
    
    # Additional test cases
    nums3 = [5, 5, 5, 1, 2, 5, 5, 5, 5]
    result3 = sol.longestSubarray(nums3)
    print(f"Test 3: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 4")
    print(f"Max value: {max(nums3)}")
    print(f"Longest consecutive sequence: [5,5,5,5] at the end")
    print()
    
    nums4 = [1, 1, 1, 1]
    result4 = sol.longestSubarray(nums4)
    print(f"Test 4: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: 4")
    print(f"All elements are the same")
    print()
    
    nums5 = [96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]
    result5 = sol.longestSubarray(nums5)
    print(f"Test 5: First 9 elements are 96317, last is 279979")
    print(f"Output: {result5}")
    print(f"Expected: 1")
    print(f"Max value: {max(nums5)}")
    print()

def demonstrate_and_property():
    print("=== Why maximum AND equals maximum element ===")
    nums = [1, 2, 3, 3, 2, 2]
    print(f"Array: {nums}")
    print("Let's check AND values of different subarrays:")
    
    max_and = 0
    best_subarray = []
    
    for i in range(len(nums)):
        current_and = nums[i]
        for j in range(i, len(nums)):
            if i == j:
                current_and = nums[i]
            else:
                current_and &= nums[j]
            
            if current_and > max_and:
                max_and = current_and
                best_subarray = nums[i:j+1]
            
            print(f"  Subarray {nums[i:j+1]} -> AND = {current_and}")
    
    print(f"Maximum AND found: {max_and}")
    print(f"Best subarray: {best_subarray}")
    print(f"Maximum element in array: {max(nums)}")
    print()

test_solution()
demonstrate_and_property()