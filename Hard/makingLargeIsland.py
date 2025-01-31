class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        island_sizes = {}
        island_id = 2  
        
        def dfs(i, j, id):
            stack = [(i, j)]
            size = 0
            while stack:
                x, y = stack.pop()
                if grid[x][y] == 1:
                    grid[x][y] = id  
                    size += 1
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            stack.append((nx, ny))
            return size
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        max_island_size = 0  
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            seen_islands.add(grid[nx][ny])
                    new_size = 1  
                    for island in seen_islands:
                        new_size += island_sizes[island]
                    max_island_size = max(max_island_size, new_size)
        
        return max(max_island_size, max(island_sizes.values()) if island_sizes else 0)


def test_solution():
    solution = Solution()
    
    # Test Case 1: Single 0 surrounded by 1s
    grid1 = [[1, 0], [0, 1]]
    print(solution.largestIsland(grid1))  
    
    # Test Case 2: All 1s in the grid
    grid2 = [[1, 1], [1, 1]]
    print(solution.largestIsland(grid2)) 
    
    # Test Case 3: Only one 0 in the grid
    grid3 = [[0]]
    print(solution.largestIsland(grid3))
    
    # Test Case 4: No 0 in the grid
    grid4 = [[1, 1], [1, 1]]
    print(solution.largestIsland(grid4)) 
    
    # Test Case 5: Multiple islands with a potential merge
    grid5 = [[1, 0, 0, 0],
             [0, 1, 0, 1],
             [0, 0, 1, 1],
             [1, 1, 0, 0]]
    print(solution.largestIsland(grid5))  

test_solution()
