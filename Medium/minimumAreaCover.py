class Solution(object):
    def minimumArea(self, grid):
        m, n = len(grid), len(grid[0])
        min_r, min_c, max_r, max_c = m, n, -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i < min_r: min_r = i
                    if j < min_c: min_c = j
                    if i > max_r: max_r = i
                    if j > max_c: max_c = j
        return (max_r - min_r + 1) * (max_c - min_c + 1)


def run_tests():
    sol = Solution()
    cases = [
        ([[0,1,0],[1,0,1]], 6),
        ([[1,0],[0,0]], 1),
        ([[1]], 1),
        ([[0,0,1,1,0]], 2),
        ([[0],[1],[1],[0]], 2),
        ([[0,0,0],[0,1,0],[0,0,0]], 1),
        ([[1,0,0,0],[0,0,0,1],[0,0,0,0]], 8),
        ([[0,0,0,1],[0,0,0,0],[1,0,0,0]], 12),
        ([[0,0,0],[0,0,0],[0,0,1]], 1),
    ]
    for grid, expected in cases:
        got = sol.minimumArea(grid)
        assert got == expected, (grid, expected, got)
    print("OK")

run_tests()
