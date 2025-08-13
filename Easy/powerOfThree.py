class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

def run_tests():
    sol = Solution()
    cases = [
        (27, True),
        (0, False),
        (-1, False),
        (1, True),
        (3, True),
        (9, True),
        (45, False),
        (2, False),
        (243, True),
        (1162261467, True),
        (1162261466, False),
    ]
    for n, expected in cases:
        got = sol.isPowerOfThree(n)
        assert got == expected, (n, expected, got)
    print("OK")

run_tests()
