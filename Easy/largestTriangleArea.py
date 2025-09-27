class Solution(object):
    def largestTriangleArea(self, points):
        def area(a, b, c):
            (x1, y1), (x2, y2), (x3, y3) = a, b, c
            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0

        n = len(points)
        best = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    best = max(best, area(points[i], points[j], points[k]))
        return best

def run_tests():
    s = Solution()
    cases = [
        ([[0,0],[0,1],[1,0],[0,2],[2,0]], 2.0),
        ([[1,0],[0,0],[0,1]], 0.5),
        ([[0,0],[1,1],[2,2],[3,3]], 0.0),
        ([[0,0],[0,3],[4,0]], 6.0),
        ([[-50,-50],[50,-50],[-50,50],[50,50]], 5000.0),
    ]
    for pts, expected in cases:
        out = s.largestTriangleArea(pts)
        assert abs(out - expected) < 1e-5, f"{pts}: expected {expected}, got {out}"
        print(f"{out:.5f}")

run_tests()
