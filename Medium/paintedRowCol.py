class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)  
        
        row_paint = [0] * m  
        col_paint = [0] * n
        for index, num in enumerate(arr):
            row, col = pos[num]  
            row_paint[row] += 1
            col_paint[col] += 1
            
            if row_paint[row] == n or col_paint[col] == m:
                return index  
        return -1 

arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
solution = Solution()
print(solution.firstCompleteIndex(arr, mat))  # Expected output: 3
