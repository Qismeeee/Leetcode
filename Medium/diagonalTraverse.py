class Solution(object):
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        res = []
        for s in range(m + n - 1):
            tmp = []
            r = 0 if s < n else s - (n - 1)
            c = s - r
            while r < m and c >= 0:
                tmp.append(mat[r][c])
                r += 1
                c -= 1
            if s % 2 == 0:
                res.extend(tmp[::-1])
            else:
                res.extend(tmp)
        return res

def run_tests():
    sol = Solution()
    cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,4,7,5,3,6,8,9]),
        ([[1,2],[3,4]], [1,2,3,4]),
        ([[1]], [1]),
        ([[1,2,3,4]], [1,2,3,4]),
        ([[1],[2],[3],[4]], [1,2,3,4]),
        ([[1,2,3],[4,5,6]], [1,2,4,5,3,6]),
        ([[1,2],[3,4],[5,6]], [1,2,3,5,4,6]),
        ([[-1,-2],[-3,-4]], [-1,-2,-3,-4]),
    ]
    for mat, expected in cases:
        got = sol.findDiagonalOrder(mat)
        assert got == expected, (mat, expected, got)
    print("OK")

run_tests()
