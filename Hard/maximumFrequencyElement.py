from bisect import bisect_left, bisect_right
from collections import Counter

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        n = len(nums)
        cnt = Counter(nums)
        uniq = sorted(cnt)

        l = 0
        W_max = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            W_max = max(W_max, r - l + 1)

        ans = min(W_max, numOperations)

        for v in uniq:
            L = bisect_left(nums, v - k)
            R = bisect_right(nums, v + k) - 1
            m = R - L + 1
            ans = max(ans, min(cnt[v] + numOperations, m))

        return ans
