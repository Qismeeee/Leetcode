class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if len(set(nums)) == n:
            return 0
        
        operations = 0
        while True:
            if len(set(nums)) == len(nums):
                return operations
            if len(nums) <= 3:
                nums = []
                operations += 1
                return operations
            else:
                nums = nums[3:]
                operations += 1