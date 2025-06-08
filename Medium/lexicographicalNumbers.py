class Solution(object):
    def lexicalOrder(self, n):
        res = []
        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur % 10 != 9 and cur + 1 <= n:
                    cur += 1
                else:
                    while cur % 10 == 9 or cur + 1 > n:
                        cur //= 10
                    cur += 1
        return res

tests = [
    (13, [1,10,11,12,13,2,3,4,5,6,7,8,9]),
    (2,  [1,2]),
    (1,  [1]),
    (20, [1,10,11,12,13,14,15,16,17,18,19,2,20,3,4,5,6,7,8,9])
]

for n, expected in tests:
    result = Solution().lexicalOrder(n)
    assert result == expected, f"n={n}: expected {expected}, got {result}"

print("All simple tests passed")
