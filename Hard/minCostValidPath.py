import heapq

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(0, 0, 0)]  # (cost, x, y)
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0

        while pq:
            cost, x, y = heapq.heappop(pq)
            if (x, y) == (m - 1, n - 1):
                return cost

            if cost > visited[x][y]:
                continue

            for i, (dx, dy) in enumerate(directions, start=1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost if grid[x][y] == i else cost + 1

                    if new_cost < visited[nx][ny]:
                        visited[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))

        return -1  

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    grid1 = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
    print("Test case 1 result:", solution.minCost(grid1))  # Expected output: 3

    # Test case 2
    grid2 = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    print("Test case 2 result:", solution.minCost(grid2))  # Expected output: 0

    # Test case 3
    grid3 = [[1, 2], [4, 3]]
    print("Test case 3 result:", solution.minCost(grid3))  # Expected output: 1
