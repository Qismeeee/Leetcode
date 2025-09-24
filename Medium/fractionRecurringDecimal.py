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
