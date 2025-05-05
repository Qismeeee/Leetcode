class Solution(object):
    def numTilings(self, n):
        MOD = 10**9+7
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[n]
    
if __name__ == "__main__":
    s = Solution()
    print(s.numTilings(1), "expected", 1)
    print(s.numTilings(2), "expected", 2)
    print(s.numTilings(3), "expected", 5)
    print(s.numTilings(4), "expected", 11)