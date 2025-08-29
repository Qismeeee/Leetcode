class Solution(object):
    def flowerGame(self, n, m):
        on = (n + 1) // 2
        en = n // 2
        om = (m + 1) // 2
        em = m // 2
        return on * em + en * om


def run_tests():
    sol = Solution()
    cases = [
        (3, 2, 3),
        (1, 1, 0),
        (2, 2, 2),
        (1, 2, 1),
        (2, 1, 1),
        (4, 5, 10),
        (5, 5, 12),
        (7, 3, 11),
        (10, 1, 5),
        (1, 10, 5),
    ]
    for n, m, expected in cases:
        got = sol.flowerGame(n, m)
        assert got == expected, (n, m, expected, got)
    print("OK")

run_tests()
