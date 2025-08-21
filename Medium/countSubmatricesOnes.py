class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            sum_min = 0
            stack = []
            for h in heights:
                width = 1
                while stack and stack[-1][0] >= h:
                    ph, pw = stack.pop()
                    sum_min -= ph * pw
                    width += pw
                sum_min += h * width
                stack.append((h, width))
                ans += sum_min
        return ans

def run_tests():
    sol = Solution()
    cases = [
        ([[1,0,1],[1,1,0],[1,1,0]], 13),
        ([[0,1,1,0],[0,1,1,1],[1,1,1,0]], 24),
        ([[1,1],[1,1]], 9),
        ([[1]], 1),
        ([[0]], 0),
        ([[1,0,1,1]], 4),
        ([[1],[1],[0],[1]], 4),
        ([[1,1,0],[1,1,1]], 12),
        ([[1,0],[1,1]], 5),
    ]
    for mat, expected in cases:
        got = sol.numSubmat(mat)
        assert got == expected, (mat, expected, got)
    print("OK")

run_tests()
