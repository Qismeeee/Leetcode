class Solution(object):
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        res = 0
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == 1:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                    res += dp[j]
                else:
                    dp[j] = 0
                prev = temp
        return res


def run_tests():
    sol = Solution()
    cases = [
        ([[0,1,1,1],[1,1,1,1],[0,1,1,1]], 15),
        ([[1,0,1],[1,1,0],[1,1,0]], 7),
        ([[1]], 1),
        ([[0]], 0),
        ([[1,1,1]], 3),
        ([[1],[1],[1]], 3),
        ([[1,1],[1,1]], 5),
        ([[1,0,1,1],[1,1,1,1]], 9),
    ]
    for mat, expected in cases:
        got = sol.countSquares(mat)
        assert got == expected, (mat, expected, got)
    print("OK")

run_tests()
