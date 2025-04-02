class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    if value > max_val:
                        max_val = value
                        
        return max_val
