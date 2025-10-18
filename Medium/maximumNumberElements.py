class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums.sort()
        cur = -10**30
        ans = 0
        for x in nums:
            L, R = x - k, x + k
            place = max(cur, L)
            if place <= R:
                ans += 1
                cur = place + 1
        return ans
