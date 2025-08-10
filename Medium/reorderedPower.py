class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = ''.join(sorted(str(n)))
        for i in range(31): 
            if ''.join(sorted(str(1 << i))) == target:
                return True
        return False


def run_tests():
    sol = Solution()
    cases = [
        (1, True),
        (10, False),
        (16, True),
        (24, False),
        (46, True),   
        (821, True),  
        (625, True), 
        (123, False),
        (128, True),
        (1000000000, False),
    ]

    for n, expected in cases:
        got = sol.reorderedPowerOf2(n)
        assert got == expected, "n=%s: expected %s, got %s" % (n, expected, got)

    print("All tests passed!")

run_tests()
