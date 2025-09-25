class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(r + 1):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
        return dp[0]
