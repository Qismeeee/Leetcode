from collections import deque
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)] 
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        
        return height

solution = Solution()

# Test case 1
isWater1 = [[0, 1], [0, 0]]
output1 = solution.highestPeak(isWater1)
print("Test Case 1:")
for row in output1:
    print(row)

# Test case 2
isWater2 = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
output2 = solution.highestPeak(isWater2)
print("\nTest Case 2:")
for row in output2:
    print(row)

# Test case 3: Edge case with all water
isWater3 = [[1]]
output3 = solution.highestPeak(isWater3)
print("\nTest Case 3:")
for row in output3:
    print(row)

# Test case 4: Edge case with a single row
isWater4 = [[0, 1, 0]]
output4 = solution.highestPeak(isWater4)
print("\nTest Case 4:")
for row in output4:
    print(row)

# Test case 5: Large case with uniform water border
isWater5 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
output5 = solution.highestPeak(isWater5)
print("\nTest Case 5:")
for row in output5:
    print(row)