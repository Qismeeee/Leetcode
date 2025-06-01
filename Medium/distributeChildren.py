class Solution(object):
    def distributeCandies(self, n, limit):
        def comb2(x):
            return x * (x - 1) // 2 if x >= 2 else 0
        total = comb2(n + 2)
        t1 = comb2(n - limit + 1) if n - limit >= 0 else 0
        t2 = comb2(n - 2 * limit) if n - 2 * limit - 1 >= 0 else 0
        t3 = comb2(n - 3 * limit - 1) if n - 3 * limit - 1 >= 2 else 0
        return total - 3 * t1 + 3 * t2 - t3

tests = [
    (5, 2, 3),
    (3, 3, 10),
    (1, 1, 3),
    (6, 2, 7)
]

s = Solution()
for n, limit, exp in tests:
    res = s.distributeCandies(n, limit)
    print(res == exp, res)
