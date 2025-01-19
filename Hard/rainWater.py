import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        trapped_water = 0
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if heightMap[nx][ny] < height:
                        trapped_water += height - heightMap[nx][ny]
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return trapped_water


def test_trapRainWater():
    solution = Solution()
    # Test Case 1
    heightMap1 = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    print(solution.trapRainWater(heightMap1)) 
    
    # Test Case 2
    heightMap2 = [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3]
    ]
    print(solution.trapRainWater(heightMap2)) 
    
    # Test Case 3 (No trapping possible)
    heightMap3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(solution.trapRainWater(heightMap3)) 
    
    # Test Case 4 (Single cell, no water)
    heightMap4 = [
        [1]
    ]
    print(solution.trapRainWater(heightMap4))  
    
    # Test Case 5 (Flat surface, no water)
    heightMap5 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(solution.trapRainWater(heightMap5))  

test_trapRainWater()
