class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0
        res = 0.0
        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            else:
                res += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                window -= dp[i - maxPts]
        return res


def run_tests():
    sol = Solution()
    eps = 1e-5
    cases = [
        (10, 1, 10, 1.0),
        (6, 1, 10, 0.6),
        (21, 17, 10, 0.73278),
        (1, 1, 2, 0.5),
        (2, 1, 2, 1.0),
        (7, 1, 10, 0.7),
        (100, 0, 10, 1.0),
        (0, 0, 1, 1.0),
    ]
    for n, k, m, expected in cases:
        got = sol.new21Game(n, k, m)
        assert abs(got - expected) <= eps, (n, k, m, expected, got)
    print("OK")

run_tests()
