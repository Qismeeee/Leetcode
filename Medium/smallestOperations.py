from collections import Counter

class Solution(object):
    def findSmallestInteger(self, nums, value):
        cnt = Counter((x % value + value) % value for x in nums)
        mex = 0
        while True:
            r = mex % value
            if cnt[r]:
                cnt[r] -= 1
                mex += 1
            else:
                return mex

nums = [1, -10, 7, 13, 6, 8]
value = 5
s = Solution()
print(s.findSmallestInteger(nums, value))

nums = [1, -10, 7, 13, 6, 8]
value = 7
print(s.findSmallestInteger(nums, value))
