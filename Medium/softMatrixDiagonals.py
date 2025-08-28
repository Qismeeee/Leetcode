class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid)
        for d in range(-(n - 1), n):
            if d >= 0:
                i, j = d, 0
            else:
                i, j = 0, -d
            vals = []
            ii, jj = i, j
            while ii < n and jj < n:
                vals.append(grid[ii][jj])
                ii += 1
                jj += 1
            vals.sort(reverse=(d >= 0))
            k = 0
            while i < n and j < n:
                grid[i][j] = vals[k]
                i += 1
                j += 1
                k += 1
        return grid


def run_tests():
    sol = Solution()
    cases = [
        ([[1,7,3],[9,8,2],[4,5,6]], [[8,2,3],[9,6,7],[4,5,1]]),
        ([[0,1],[1,2]], [[2,1],[1,0]]),
        ([[1]], [[1]]),
        ([[5,5],[5,5]], [[5,5],[5,5]]),
        ([[-1,0],[0,-1]], [[-1,0],[0,-1]]),
        ([[1,0,0],[0,1,0],[0,0,1]], [[1,0,0],[0,1,0],[0,0,1]]),
    ]
    for grid, expected in cases:
        got = sol.sortMatrix([row[:] for row in grid])
        assert got == expected, (grid, expected, got)
    print("OK")

run_tests()
