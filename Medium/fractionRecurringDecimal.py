class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        n, d = abs(numerator), abs(denominator)

        int_part = n // d
        rem = n % d
        if rem == 0:
            return sign + str(int_part)

        res = [sign + str(int_part), '.']
        pos = {}  # remainder -> index in res

        while rem != 0:
            if rem in pos:
                idx = pos[rem]
                res.insert(idx, '(')
                res.append(')')
                break
            pos[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d

        return ''.join(res)


def run_tests():
    s = Solution()
    cases = [
        (1, 2, "0.5"),
        (2, 1, "2"),
        (4, 333, "0.(012)"),
        (1, 3, "0.(3)"),
        (1, 6, "0.1(6)"),
        (50, 8, "6.25"),
        (-1, 2, "-0.5"),
        (-22, 7, "-3.(142857)"),
        (0, 7, "0"),
        (1, 250, "0.004"),
        (1, 90, "0.0(1)"),
    ]
    for num, den, expected in cases:
        out = s.fractionToDecimal(num, den)
        assert out == expected, f"{num}/{den}: expected {expected}, got {out}"
        print(f"{num}/{den} -> {out}")

run_tests()