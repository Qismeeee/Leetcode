class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        cur = 0
        for ch in s:
            if ch == '1':
                cur += 1
                ans += cur
            else:
                cur = 0
        return ans % MOD


s = Solution()
print(s.numSub("0110111"))  # 9
print(s.numSub("101"))      # 2
print(s.numSub("111111"))   # 21
print(s.numSub("0"))        # 0
print(s.numSub("1"))        # 1
