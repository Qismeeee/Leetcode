class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_diff = 0
        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])
            if diff > max_diff:
                max_diff = diff
        return max_diff

print(Solution().maxAdjacentDistance([1, 2, 4]))      
print(Solution().maxAdjacentDistance([-5, -10, -5]))