class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        best_d2 = -1
        best_area = 0
        for l, w in dimensions:
            d2 = l * l + w * w
            area = l * w
            if d2 > best_d2 or (d2 == best_d2 and area > best_area):
                best_d2 = d2
                best_area = area
        return best_area

def run_tests():
    sol = Solution()
    cases = [
        ([[9,3],[8,6]], 48),
        ([[3,4],[4,3]], 12),
        ([[1,1]], 1),
        ([[6,8],[8,6]], 48),
        ([[1,7],[5,5]], 25),
        ([[10,1],[7,7]], 10),
        ([[100,100],[100,99]], 10000),
        ([[2,9],[9,2],[6,7]], 42),
    ]
    for dims, expected in cases:
        got = sol.areaOfMaxDiagonal(dims)
        assert got == expected, (dims, expected, got)
    print("OK")

run_tests()
