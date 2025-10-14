class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        inc = [1]*n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc[i] = inc[i-1] + 1
        for a in range(0, n - 2*k + 1):
            if inc[a + k - 1] >= k and inc[a + 2*k - 1] >= k:
                return True
        return False
