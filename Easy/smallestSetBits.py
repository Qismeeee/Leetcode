class Solution(object):
    def smallestNumber(self, n):
        x = 1
        while x < n:
            x = (x << 1) | 1
        return x

n = 5
s = Solution()
print(s.smallestNumber(n))  # 7

n = 10
print(s.smallestNumber(n))  # 15

n = 3
print(s.smallestNumber(n))  # 3
