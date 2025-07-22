class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0
        
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
class Solution2(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_to_index = {}
        left = 0
        current_sum = 0
        max_sum = 0
        
        for right in range(len(nums)):
            if nums[right] in num_to_index and num_to_index[nums[right]] >= left:
                for i in range(left, num_to_index[nums[right]] + 1):
                    current_sum -= nums[i]
                left = num_to_index[nums[right]] + 1
            num_to_index[nums[right]] = right
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        
        return max_sum


def test_solution():
    sol = Solution()
    sol2 = Solution2()
    
    test_cases = [
        [4, 2, 4, 5, 6],        
        [5, 2, 1, 2, 5, 2, 1, 2, 5], 
        [1, 2, 3, 4, 5],        
        [1, 1, 1, 1, 1],       
        [1, 2, 1, 3, 4],       
        [10],                  
    ]
    
    for i, nums in enumerate(test_cases):
        result1 = sol.maximumUniqueSubarray(nums)
        result2 = sol2.maximumUniqueSubarray(nums)
        print("Test {}: nums = {} -> Result: {} (Match: {})".format(
            i+1, nums, result1, result1 == result2))

test_solution()