class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        inc = [1]*n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc[i] = inc[i-1] + 1

        def ok(k):
            if k == 0: 
                return True
            for a in range(0, n - 2*k + 1):
                if inc[a + k - 1] >= k and inc[a + 2*k - 1] >= k:
                    return True
            return False

        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
