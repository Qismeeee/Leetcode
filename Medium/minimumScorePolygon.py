class Solution(object):
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for length in range(3, n+1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = float('inf')
                for k in range(i+1, j):
                    best = min(best, dp[i][k] + dp[k][j] + values[i]*values[k]*values[j])
                dp[i][j] = best
        return dp[0][n-1]


def run_tests():
    s = Solution()
    cases = [
        ([1,2,3], 6),
        ([3,7,4,5], 144),
        ([1,3,1,4,1,5], 13),
        ([2,2,2,2], 16),
        ([5,4,3], 60),
        ([1,1,1,1,1], 3),
    ]
    for vals, expected in cases:
        out = s.minScoreTriangulation(vals)
        assert out == expected, f"{vals}: expected {expected}, got {out}"
        print(vals, out)

run_tests()
