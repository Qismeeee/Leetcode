class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * k for _ in range(n)]

        # initialize (0,0)
        dp[0][grid[0][0] % k] = 1
        for j in range(1, n):
            val = grid[0][j]
            ndp = [0] * k
            for r in range(k):
                if dp[j-1][r]:
                    nr = (r + val) % k
                    ndp[nr] = (ndp[nr] + dp[j-1][r]) % MOD
            dp[j] = ndp

        # process remaining rows
        for i in range(1, m):
            new_dp0 = [0] * k
            val = grid[i][0]
            # first column: can only come from top (same column)
            for r in range(k):
                if dp[0][r]:
                    nr = (r + val) % k
                    new_dp0[nr] = (new_dp0[nr] + dp[0][r]) % MOD
            dp[0] = new_dp0

            # rest of columns
            for j in range(1, n):
                val = grid[i][j]
                ndp = [0] * k
                # from top: dp[j][r]
                for r in range(k):
                    if dp[j][r]:
                        nr = (r + val) % k
                        ndp[nr] = (ndp[nr] + dp[j][r]) % MOD
                # from left: dp[j-1][r] (already updated for current row)
                for r in range(k):
                    if dp[j-1][r]:
                        nr = (r + val) % k
                        ndp[nr] = (ndp[nr] + dp[j-1][r]) % MOD
                dp[j] = ndp

        return dp[n-1][0] % MOD
