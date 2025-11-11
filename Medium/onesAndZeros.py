class Solution(object):
    def findMaxForm(self, strs, m, n):
        # dp[i][j] = max number of strings using at most i zeros and j ones
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros

            # 0-1 knapsack: iterate backwards
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j],
                                   dp[i-zeros][j-ones] + 1)

        return dp[m][n]

s = Solution()

strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(s.findMaxForm(strs, m, n))  # 4

strs = ["10","0","1"]
m = 1
n = 1
print(s.findMaxForm(strs, m, n))  # 2
