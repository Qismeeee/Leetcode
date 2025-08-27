class Solution(object):
    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])

        if not any(1 in row for row in grid):
            return 0
        dr = (-1, 1, 1, -1)
        dc = (1, 1, -1, -1)
        cw = (1, 2, 3, 0) 
        dp2 = [[[0]*n for _ in range(m)] for _ in range(4)]
        dp0 = [[[0]*n for _ in range(m)] for _ in range(4)]
        dp1 = [[[0]*n for _ in range(m)] for _ in range(4)]

        endlen = [[[0]*n for _ in range(m)] for _ in range(4)]
        def inb(i, j): return 0 <= i < m and 0 <= j < n
        for d in range(4):
            rstep, cstep = -dr[d], -dc[d]  
            if d == 0:  
                for j0 in range(n):
                    i, j = 0, j0
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep 
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:  # 1
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep
                for i0 in range(1, m):
                    i, j = i0, n-1
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep

            elif d == 1:  # SE
                for j0 in range(n):
                    i, j = m-1, j0
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep
                for i0 in range(m-2, -1, -1):
                    i, j = i0, n-1
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep

            elif d == 2:  # SW
                for j0 in range(n):
                    i, j = m-1, j0
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep
                for i0 in range(m-2, -1, -1):
                    i, j = i0, 0
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep

            else:  # d == 3, NW
                for j0 in range(n):
                    i, j = 0, j0
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep
                for i0 in range(1, m):
                    i, j = i0, 0
                    while inb(i, j):
                        ni, nj = i - rstep, j - cstep
                        if grid[i][j] == 2:
                            dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)
                        elif grid[i][j] == 0:
                            dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        else:
                            dp1[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                        i += rstep; j += cstep

        for d in range(4):
            rstep, cstep = dr[d], dc[d]
            if d == 0: 
                for j0 in range(n):
                    i, j = m-1, j0
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep
                for i0 in range(m-2, -1, -1):
                    i, j = i0, 0
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep

            elif d == 1:  # SE
                for j0 in range(n):
                    i, j = 0, j0
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep
                for i0 in range(1, m):
                    i, j = i0, 0
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep

            elif d == 2:  # SW
                for j0 in range(n-1, -1, -1):
                    i, j = 0, j0
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep
                for i0 in range(1, m):
                    i, j = i0, n-1
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep

            else:  # d == 3, NW
                for j0 in range(n-1, -1, -1):
                    i, j = m-1, j0
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep
                for i0 in range(m-2, -1, -1):
                    i, j = i0, n-1
                    Lp = 0
                    while inb(i, j):
                        expected = 1 if Lp == 0 else (2 if (Lp & 1) else 0)
                        if grid[i][j] == expected:
                            Lp += 1
                        else:
                            Lp = 1 if grid[i][j] == 1 else 0
                        endlen[d][i][j] = Lp
                        i += rstep; j += cstep

        ans = 0

        for d in range(4):
            D = dp1[d]
            for i in range(m):
                row = D[i]
                for j in range(n):
                    if row[j] > ans:
                        ans = row[j]

        for d in range(4):
            d2 = cw[d]
            for i in range(m):
                for j in range(n):
                    L1 = endlen[d][i][j]
                    if L1 == 0:
                        continue
                    ni, nj = i + dr[d2], j + dc[d2]
                    if not inb(ni, nj):
                        if L1 > ans:
                            ans = L1
                        continue
                    if (L1 & 1) == 1:
                        L2 = dp2[d2][ni][nj]
                    else:
                        L2 = dp0[d2][ni][nj]
                    total = L1 + L2
                    if total > ans:
                        ans = total

        return ans

def run_tests():
    sol = Solution()
    cases = [
        (
            [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]],
            5
        ),
        (
            [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]],
            4
        ),
        (
            [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]],
            5
        ),
        ([[1]], 1),
        ([[2,0],[0,2]], 0),
        ([[1,2,0,2]], 1),
        ([[1,0],[0,2]], 2),
        (
            [[0,1,0],[0,0,2],[2,0,0]],
            3
        ),
        (
            [[1,2,0],[2,0,2],[0,2,0]],
            2
        ),
    ]
    for grid, expected in cases:
        got = sol.lenOfVDiagonal(grid)
        assert got == expected, (grid, expected, got)
    print("OK")

run_tests()
