import unittest

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    result += 1

        return result
    
class TestCountServers(unittest.TestCase):
    def test_no_communication(self):
        grid = [[1, 0], [0, 1]]
        self.assertEqual(Solution().countServers(grid), 0)

    def test_all_communicate(self):
        grid = [[1, 0], [1, 1]]
        self.assertEqual(Solution().countServers(grid), 3)

    def test_some_communicate(self):
        grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(Solution().countServers(grid), 4)

if __name__ == '__main__':
    unittest.main()