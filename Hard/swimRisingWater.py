import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (elevation, row, col)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while heap:
            elevation, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return elevation
            if visited[r][c]:
                continue
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    next_elevation = max(elevation, grid[nr][nc])
                    heapq.heappush(heap, (next_elevation, nr, nc))
