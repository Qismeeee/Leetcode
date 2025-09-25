class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(r + 1):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
        return dp[0]


def run_tests():
    s = Solution()
    cases = [
        ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
        ([[-10]], -10),
        ([[1],[2,3],[4,5,6]], 7),
        ([[5],[9,6],[4,6,8],[0,7,1,5]], 14),
        ([[2],[3,4],[6,5,7],[4,1,8,3],[3,2,1,2,3]], 12),
    ]
    for tri, expected in cases:
        out = s.minimumTotal(tri)
        assert out == expected, f"{tri}: expected {expected}, got {out}"
        print(out)

run_tests()
