class Solution(object):
    def getNoZeroIntegers(self, n):
        def no_zero(x):
            return '0' not in str(x)
        for a in range(1, n):
            b = n - a
            if no_zero(a) and no_zero(b):
                return [a, b]

def no_zero(x):
    return '0' not in str(x)

tests = [2, 11, 20, 101, 109, 1000, 9999]
s = Solution()
for n in tests:
    a, b = s.getNoZeroIntegers(n)
    assert a + b == n
    assert no_zero(a) and no_zero(b)
    print(n, [a, b])
