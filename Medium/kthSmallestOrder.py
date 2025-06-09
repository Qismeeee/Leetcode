class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps

        cur = 1
        k -= 1 
        while k > 0:
            steps = count_steps(n, cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur


tests = [
    (13, 2, 10),
    (13, 6, 2),
    (1, 1, 1),
    (100, 10, 17), 
    (1000, 100, None) 
]

for n, k, expected in tests:
    result = Solution().findKthNumber(n, k)
    if expected is not None:
        assert result == expected, f"n={n}, k={k}: expected {expected}, got {result}"
    print(f"n={n}, k={k} -> {result}")

print("All specified tests passed (for those with a known expected value).")