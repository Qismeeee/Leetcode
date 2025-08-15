class Solution(object):
    def isPowerOfFour(self, n):
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

def run_tests():
    sol = Solution()
    cases = [
        (16, True),
        (5, False),
        (1, True),
        (0, False),
        (-4, False),
        (4, True),
        (64, True),
        (8, False),
        (1073741824, True),
        (2147483647, False),
    ]
    for n, expected in cases:
        got = sol.isPowerOfFour(n)
        assert got == expected, (n, expected, got)
    print("OK")

run_tests()
