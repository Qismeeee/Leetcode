class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        longest = 1
        current_increasing = 1
        current_decreasing = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_increasing += 1
                current_decreasing = 1  
            elif nums[i] < nums[i - 1]:
                current_decreasing += 1
                current_increasing = 1  
            else:
                current_increasing = 1
                current_decreasing = 1
            longest = max(longest, current_increasing, current_decreasing)
        
        return longest


sol = Solution()
print(sol.longestMonotonicSubarray([1, 4, 3, 3, 2]))  
print(sol.longestMonotonicSubarray([3, 3, 3, 3])) 
print(sol.longestMonotonicSubarray([3, 2, 1])) 