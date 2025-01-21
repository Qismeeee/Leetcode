class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]

        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
        min_second_robot = float('inf')

        for col in range(n):
            top_points = top_prefix[-1] - top_prefix[col] if col < n - 1 else 0
            bottom_points = bottom_prefix[col - 1] if col > 0 else 0
            second_robot_points = max(top_points, bottom_points)
            min_second_robot = min(min_second_robot, second_robot_points)

        return min_second_robot

def test_solution():
    solution = Solution()
    # Test case 1: Small grid
    grid = [[2, 5, 4], [1, 5, 1]]
    print("Test Case 1 Output:", solution.gridGame(grid))  # Expected: 4

    # Test case 2: Small grid with equal values
    grid = [[3, 3, 1], [8, 5, 2]]
    print("Test Case 2 Output:", solution.gridGame(grid))  # Expected: 4

    # Test case 3: Larger grid
    grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
    print("Test Case 3 Output:", solution.gridGame(grid))  # Expected: 7

    # Test case 4: Single column grid
    grid = [[5], [10]]
    print("Test Case 4 Output:", solution.gridGame(grid))  # Expected: 0

    # Test case 5: Single row grid
    grid = [[10, 20, 30], [1, 2, 3]]
    print("Test Case 5 Output:", solution.gridGame(grid))  # Expected: 3

test_solution()