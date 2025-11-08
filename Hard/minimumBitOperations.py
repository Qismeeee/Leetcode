class Solution(object):
    def minimumOneBitOperations(self, n):
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans
