class Solution(object):
    def __init__(self, nums):
        self.arr = nums
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        res = nums[0]

        for n in nums:
            if total < 0:
                total = 0
            total += n
            res = max(res, total)
        return res
    
# Test

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution(nums)
print(sol.maxSubArray(nums))




