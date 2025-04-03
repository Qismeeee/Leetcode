class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = 0
        result = 0
        max_i = nums[0]

        for j in range(1, len(nums) - 1):
            max_diff = max(max_diff, max_i - nums[j])
            result = max(result, max_diff * nums[j + 1])
            max_i = max(max_i, nums[j])

        return result
