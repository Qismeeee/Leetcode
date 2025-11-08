class Solution(object):
    def minimumOneBitOperations(self, n):
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans


s = Solution()
print(s.minimumOneBitOperations(3))  # 2
print(s.minimumOneBitOperations(6))  # 4
print(s.minimumOneBitOperations(0))  # 0
