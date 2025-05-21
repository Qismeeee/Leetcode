class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if first_col_zero:
                matrix[i][0] = 0


def test():
    s = Solution()
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix1)
    assert matrix1 == [[1,0,1],[0,0,0],[1,0,1]]
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix2)
    assert matrix2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print("All tests passed")

if __name__ == "__main__":
    test()
