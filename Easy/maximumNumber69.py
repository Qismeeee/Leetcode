class Solution(object):
    def maximum69Number(self, num):
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        return int(''.join(s))

def run_tests():
    sol = Solution()
    cases = [
        (9669, 9969),
        (9996, 9999),
        (9999, 9999),
        (6, 9),
        (9, 9),
        (6699, 9699),
        (9966, 9996),
        (6969, 9969),
        (6666, 9666),
        (6966, 9966),
    ]
    for num, expected in cases:
        got = sol.maximum69Number(num)
        assert got == expected, (num, expected, got)
    print("OK")

run_tests()
