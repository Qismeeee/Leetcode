class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        r = 0
        for length in range(1, k + 1):
            r = (r * 10 + 1) % k
            if r == 0:
                return length
        return -1

s = Solution()

print(s.smallestRepunitDivByK(1))   # 1
print(s.smallestRepunitDivByK(2))   # -1
print(s.smallestRepunitDivByK(3))   # 3
print(s.smallestRepunitDivByK(7))   # 6   (111111 % 7 == 0)
print(s.smallestRepunitDivByK(13))  # 6   (111111 % 13 == 0)
