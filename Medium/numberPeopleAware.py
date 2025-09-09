class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0
        for day in range(2, n + 1):
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            dp[day] = share
        return sum(dp[max(1, n - forget + 1): n + 1]) % MOD

def run_tests():
    s = Solution()
    cases = [
        (6, 2, 4, 5),
        (4, 1, 3, 6),
        (2, 1, 2, 1),
        (7, 2, 4, 6),
        (10, 2, 4, None),
        (15, 3, 6, None),
    ]
    for n, d, f, expected in cases:
        res = s.peopleAwareOfSecret(n, d, f)
        if expected is not None:
            assert res == expected, "fail"
        print((n, d, f), res)

run_tests()
