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
