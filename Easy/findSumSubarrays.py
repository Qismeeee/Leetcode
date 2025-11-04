from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            items = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)
            cur = 0
            taken = 0
            for val, cnt in items:
                if taken == x:
                    break
                cur += val * cnt
                taken += 1
            res.append(cur)
        return res
