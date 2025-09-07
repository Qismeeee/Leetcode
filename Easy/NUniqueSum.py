class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        if n % 2 != 0:
            result.append(0)
        return result

def test_sumZero():
    s = Solution()

    test_cases = [
        (1, [0]),
        (2, [-1, 1]),
        (3, [-1, 0, 1]),
        (4, [-1, 1, -2, 2]),
        (5, [-2, -1, 0, 1, 2])
    ]

    for n, expected_sum_zero in test_cases:
        result = s.sumZero(n)
        assert len(result) == n, f"❌ Failed length check for n={n}: got {len(result)}"
        assert len(set(result)) == n, f"❌ Failed uniqueness check for n={n}: got duplicates in {result}"
        assert sum(result) == 0, f"❌ Failed sum check for n={n}: sum is {sum(result)}"
        print(f"✅ Test passed for n={n}: {result}")

# Gọi test
test_sumZero()
