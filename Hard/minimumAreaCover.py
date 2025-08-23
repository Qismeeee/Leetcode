class Solution(object):
    def minimumSum(self, grid):
        m, n = len(grid), len(grid[0])
        INF = 10**18
        areaCols = [[0]*n for _ in range(n)]
        minTwoHorizCols = [[INF]*n for _ in range(n)]

        for L in range(n):
            for R in range(L, n):
                width = R - L + 1

                # prefix over rows: top part [0..r]
                colHas = [False] * width
                minc, maxc = n, -1
                minr, maxr = m, -1
                pref = [0]*m
                for r in range(m):
                    row_has = False
                    for c in range(L, R+1):
                        if grid[r][c] == 1:
                            row_has = True
                            idx = c - L
                            if not colHas[idx]:
                                colHas[idx] = True
                                if c < minc: minc = c
                                if c > maxc: maxc = c
                    if row_has:
                        if r < minr: minr = r
                        if r > maxr: maxr = r
                    if maxr == -1:
                        pref[r] = 1
                    else:
                        pref[r] = (maxr - minr + 1) * (maxc - minc + 1)

                # suffix over rows: bottom part [r+1..m-1]
                colHas = [False] * width
                minc2, maxc2 = n, -1
                minr2, maxr2 = m, -1
                suff = [0]*m
                for r in range(m-1, -1, -1):
                    row_has = False
                    for c in range(L, R+1):
                        if grid[r][c] == 1:
                            row_has = True
                            idx = c - L
                            if not colHas[idx]:
                                colHas[idx] = True
                                if c < minc2: minc2 = c
                                if c > maxc2: maxc2 = c
                    if row_has:
                        if r < minr2: minr2 = r
                        if r > maxr2: maxr2 = r
                    if maxr2 == -1:
                        suff[r] = 1
                    else:
                        suff[r] = (maxr2 - minr2 + 1) * (maxc2 - minc2 + 1)

                areaCols[L][R] = pref[m-1]
                best = INF
                if m >= 2:
                    for r in range(m-1):
                        s = pref[r] + suff[r+1]
                        if s < best: best = s
                else:
                    # two rectangles in one row band: force two vertical 1x1 (area 2)
                    best = 2
                minTwoHorizCols[L][R] = best

        areaRows = [[0]*m for _ in range(m)]
        minTwoVertRows = [[INF]*m for _ in range(m)]

        for T in range(m):
            for B in range(T, m):
                height = B - T + 1

                # prefix over columns: left part [0..c]
                rowHas = [False] * height
                minr, maxr = m, -1
                minc, maxc = n, -1
                pref = [0]*n
                for c in range(n):
                    col_has = False
                    for r in range(T, B+1):
                        if grid[r][c] == 1:
                            col_has = True
                            idx = r - T
                            if not rowHas[idx]:
                                rowHas[idx] = True
                                if r < minr: minr = r
                                if r > maxr: maxr = r
                    if col_has:
                        if c < minc: minc = c
                        if c > maxc: maxc = c
                    if maxc == -1:
                        pref[c] = 1
                    else:
                        pref[c] = (maxr - minr + 1) * (maxc - minc + 1)

                # suffix over columns: right part [c+1..n-1]
                rowHas = [False] * height
                minr2, maxr2 = m, -1
                minc2, maxc2 = n, -1
                suff = [0]*n
                for c in range(n-1, -1, -1):
                    col_has = False
                    for r in range(T, B+1):
                        if grid[r][c] == 1:
                            col_has = True
                            idx = r - T
                            if not rowHas[idx]:
                                rowHas[idx] = True
                                if r < minr2: minr2 = r
                                if r > maxr2: maxr2 = r
                    if col_has:
                        if c < minc2: minc2 = c
                        if c > maxc2: maxc2 = c
                    if maxc2 == -1:
                        suff[c] = 1
                    else:
                        suff[c] = (maxr2 - minr2 + 1) * (maxc2 - minc2 + 1)

                areaRows[T][B] = pref[n-1]
                best = INF
                if n >= 2:
                    for c in range(n-1):
                        s = pref[c] + suff[c+1]
                        if s < best: best = s
                else:
                    best = 2
                minTwoVertRows[T][B] = best

        ans = INF

        # Three vertical stripes
        if n >= 3:
            for i in range(n-2):
                for j in range(i+1, n-1):
                    total = areaCols[0][i] + areaCols[i+1][j] + areaCols[j+1][n-1]
                    if total < ans: ans = total

        # Three horizontal stripes
        if m >= 3:
            for i in range(m-2):
                for j in range(i+1, m-1):
                    total = areaRows[0][i] + areaRows[i+1][j] + areaRows[j+1][m-1]
                    if total < ans: ans = total

        # Vertical first cut, then horizontal inside one side (2+1)
        if n >= 2:
            for c in range(n-1):
                total = minTwoHorizCols[0][c] + areaCols[c+1][n-1]
                if total < ans: ans = total
                total = areaCols[0][c] + minTwoHorizCols[c+1][n-1]
                if total < ans: ans = total

        # Horizontal first cut, then vertical inside one side (2+1)
        if m >= 2:
            for r in range(m-1):
                total = minTwoVertRows[0][r] + areaRows[r+1][m-1]
                if total < ans: ans = total
                total = areaRows[0][r] + minTwoVertRows[r+1][m-1]
                if total < ans: ans = total

        return ans


def run_tests():
    sol = Solution()
    cases = [
        ([[1,0,1],[1,1,1]], 5),
        ([[1,0,1,0],[0,1,0,1]], 5),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
        ([[1],[1],[1],[1]], 4),
        ([[1,0,1],[1,0,1]], 4),
        ([[0,1,0],[1,1,1],[0,1,0]], 5),
        ([[1,0,1,0,1]], 3),
        ([[1,0,1,0,1,0,1]], 5),
    ]
    for grid, expected in cases:
        got = sol.minimumSum(grid)
        assert got == expected, (grid, expected, got)
    print("OK")

run_tests()
