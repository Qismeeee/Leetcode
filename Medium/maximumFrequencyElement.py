from bisect import bisect_left, bisect_right
from collections import Counter

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        n = len(nums)
        cnt = Counter(nums)
        uniq = sorted(cnt)

        # W_max: max number of elements in any interval of length ≤ 2k
        l = 0
        W_max = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            W_max = max(W_max, r - l + 1)
        ans = min(W_max, numOperations)  # targets not necessarily in nums

        # Consider targets t that are existing values v
        for v in uniq:
            L = bisect_left(nums, v - k)
            R = bisect_right(nums, v + k) - 1
            W_v = R - L + 1
            ans = max(ans, min(W_v, cnt[v] + numOperations))

        return ans

nums = [1,4,5]; k = 1; numOperations = 2
s = Solution()
print(s.maxFrequency(nums, k, numOperations))  # 2

nums = [5,11,20,20]; k = 5; numOperations = 1
print(s.maxFrequency(nums, k, numOperations))  # 2

nums = [4,4,4,4]; k = 1; numOperations = 0
print(s.maxFrequency(nums, k, numOperations))  # 4

nums = [1,10,10,10,20]; k = 5; numOperations = 1
print(s.maxFrequency(nums, k, numOperations))  # 4
