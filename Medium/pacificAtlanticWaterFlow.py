class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= m or c < 0 or c >= n or
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(r+dr, c+dc, visited, heights[r][c])
        
        # Pacific Ocean (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
        
        # Atlantic Ocean (bottom row and right column)
        for i in range(m):
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):
            dfs(m-1, j, atlantic, heights[m-1][j])
        
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result


def test_pacific_atlantic():
    solution = Solution()
    
    heights = [
        [1, 2],
        [4, 3]
    ]
    
    expected_output = [[0,1], [1,0], [1,1]]
    result = solution.pacificAtlantic(heights)
    assert set(map(tuple, result)) == set(map(tuple, expected_output)), f"Failed test case. Got: {result}"
    print("✅ Test case passed!")

test_pacific_atlantic()
