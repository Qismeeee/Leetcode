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
