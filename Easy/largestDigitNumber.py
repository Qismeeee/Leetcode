class Solution(object):
    def largestGoodInteger(self, num):
        for d in "9876543210":
            t = d * 3
            if t in num:
                return t
        return ""


def run_tests():
    sol = Solution()
    cases = [
        ("6777133339", "777"),
        ("2300019", "000"),
        ("42352338", ""),
        ("111", "111"),
        ("999", "999"),
        ("1000", "000"),
        ("5555", "555"),
        ("123", ""),
        ("909090", ""),
        ("090909000", "000"),
        ("000", "000"),
    ]
    for s, expected in cases:
        got = sol.largestGoodInteger(s)
        assert got == expected, (s, expected, got)
    print("OK")

run_tests()
