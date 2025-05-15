class Solution(object):
    def getLongestSubsequence(self, words, groups):
        dp0, dp1 = [], []
        for w, g in zip(words, groups):
            if g == 0:
                new0 = dp1 + [w]
                if len(new0) > len(dp0):
                    dp0 = new0
            else:
                new1 = dp0 + [w]
                if len(new1) > len(dp1):
                    dp1 = new1
        return dp0 if len(dp0) >= len(dp1) else dp1

words = ["a","b","c","d"]
groups = [1,0,1,1]
print(Solution().getLongestSubsequence(words, groups))
