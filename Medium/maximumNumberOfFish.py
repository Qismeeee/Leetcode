import unittest

class Solution(object):
    def findMaxFish(self, grid):
        """
      :type grid: List[List[int]]
      :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid)
        max_fish = 0

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            fish = grid[row][col]
            grid[row][col] = 0  
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                fish += dfs(row + dr, col + dc)
            return fish

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish
    

class TestFindMaxFish(unittest.TestCase):
    def test_no_water_cells(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(Solution().findMaxFish(grid), 0)

    def test_single_water_cell(self):
        grid = [[0, 1, 0], [0, 0, 0]]
        self.assertEqual(Solution().findMaxFish(grid), 1)

    def test_multiple_water_cells(self):
        grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
        self.assertEqual(Solution().findMaxFish(grid), 7)

    def test_disconnected_water_cells(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        self.assertEqual(Solution().findMaxFish(grid), 1)

if __name__ == '__main__':
    unittest.main()