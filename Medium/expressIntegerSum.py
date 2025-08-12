class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        vals = []
        k = 1
        while True:
            v = k ** x
            if v > n:
                break
            vals.append(v)
            k += 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for v in vals:
            for s in range(n, v - 1, -1):
                dp[s] = (dp[s] + dp[s - v]) % MOD
        return dp[n]

def run_tests():
    sol = Solution()
    cases = [
        (10, 2, 1),
        (4, 1, 2),
        (1, 5, 1),
        (2, 1, 1),
        (100, 2, 3),
        (100, 3, 1),
        (160, 3, 1),
        (13, 2, 1),
        (50, 2, 3),
        (3, 2, 0),
        (5, 2, 1),
        (9, 2, 1),
        (25, 2, 2),
        (5, 1, 3),
        (33, 5, 1),
    ]
    for n, x, expected in cases:
        got = sol.numberOfWays(n, x)
        assert got == expected, (n, x, expected, got)
    print("OK")

run_tests()
