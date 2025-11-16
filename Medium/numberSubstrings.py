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
