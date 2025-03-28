import heapq
from collections import deque

class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        indexed_queries = [(q, i) for i, q in enumerate(queries)]
        sorted_queries = sorted(indexed_queries)
        
        priority_queue = [(grid[0][0], 0, 0)]  
        visited = set()
        points = 0

        query_results = {}
        query_idx = 0
        
        while priority_queue and query_idx < len(sorted_queries):
            cell_value, row, col = heapq.heappop(priority_queue)
            while query_idx < len(sorted_queries) and sorted_queries[query_idx][0] <= cell_value:
                query_value, original_idx = sorted_queries[query_idx]
                query_results[original_idx] = 0 if query_value <= grid[0][0] else points
                query_idx += 1
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            points += 1
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(priority_queue, (grid[nr][nc], nr, nc))
        
        while query_idx < len(sorted_queries):
            query_value, original_idx = sorted_queries[query_idx]
            query_results[original_idx] = 0 if query_value <= grid[0][0] else points
            query_idx += 1
        
        return [query_results[i] for i in range(len(queries))]
    

solution = Solution()
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
result = solution.maxPoints(grid, queries)

print(f"Grid: {grid}")
print(f"Queries: {queries}")
print(f"Kết quả: {result}")