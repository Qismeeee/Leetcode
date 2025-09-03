class Solution(object):
    def numberOfPairs(self, points):
        n = len(points)
        xs = sorted({x for x, y in points})
        ys = sorted({y for x, y in points})
        xi = {x: i for i, x in enumerate(xs)}
        yi = {y: i for i, y in enumerate(ys)}
        ux, uy = len(xs), len(ys)

        grid = [[0] * uy for _ in range(ux)]
        idx = []
        for x, y in points:
            ix, iy = xi[x], yi[y]
            grid[ix][iy] = 1
            idx.append((ix, iy))

        ps = [[0] * (uy + 1) for _ in range(ux + 1)]
        for i in range(ux):
            row_ps = ps[i + 1]
            row_prev = ps[i]
            gi = grid[i]
            s = 0
            for j in range(uy):
                s += gi[j]
                row_ps[j + 1] = s + row_prev[j + 1]

        ans = 0
        for a in range(n):
            ax, ay = idx[a]
            for b in range(n):
                if a == b:
                    continue
                bx, by = idx[b]
                if ax <= bx and ay >= by:
                    s = ps[bx + 1][ay + 1] - ps[ax][ay + 1] - ps[bx + 1][by] + ps[ax][by]
                    if s == 2:
                        ans += 1
        return ans


def run_tests():
    sol = Solution()
    cases = [
        ([[1,1],[2,2],[3,3]], 0),
        ([[6,2],[4,4],[2,6]], 2),
        ([[3,1],[1,3],[1,1]], 2),
        ([[0,0],[1,0],[2,0]], 2),
        ([[0,2],[2,0],[1,1]], 0),
        ([[0,0],[3,0],[1,1],[2,2]], 1),
        ([[0,3],[0,1],[0,2]], 2),
        ([[-1,1],[0,0],[1,-1]], 2),
    ]
    for pts, expected in cases:
        got = sol.numberOfPairs(pts)
        assert got == expected, (pts, expected, got)
    print("OK")

run_tests()
