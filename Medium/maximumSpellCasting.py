import bisect
from collections import Counter

class Solution(object):
    def maximumTotalDamage(self, power):
        cnt = Counter(power)
        vals = sorted(cnt)
        weights = [v * cnt[v] for v in vals]
        dp = [0] * (len(vals) + 1)
        for i, v in enumerate(vals, 1):
            j = bisect.bisect_left(vals, v - 2) - 1
            take = weights[i - 1] + (dp[j + 1] if j >= 0 else 0)
            dp[i] = max(dp[i - 1], take)
        return dp[-1]

power = [1,1,3,4]
s = Solution()
print(s.maximumTotalDamage(power))
