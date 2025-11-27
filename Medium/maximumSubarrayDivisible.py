class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        INF = 10**30
        # min_prefix[r] = minimum prefix sum seen so far with index % k == r
        min_prefix = [INF] * k
        min_prefix[0] = 0  # prefix at index 0 has sum 0 and 0 % k == 0

        ans = -INF
        for j in range(1, n + 1):
            r = j % k
            # subarray (i..j-1) has length divisible by k iff i % k == j % k
            if min_prefix[r] != INF:
                ans = max(ans, pref[j] - min_prefix[r])
            # update minimum prefix for this remainder
            if pref[j] < min_prefix[r]:
                min_prefix[r] = pref[j]

        return ans
