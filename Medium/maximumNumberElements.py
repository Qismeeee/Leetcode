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

nums = [1, 2, 2, 3, 3, 4]
k = 2
s = Solution()
print(s.maxDistinctElements(nums, k))

nums = [4, 4, 4, 4]
k = 1
print(s.maxDistinctElements(nums, k))
