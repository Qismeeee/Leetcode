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

nums = [2,5,7,8,9,2,3,4,3,1]
k = 3
s = Solution()
print(s.hasIncreasingSubarrays(nums, k))
