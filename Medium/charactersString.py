class Solution(object):
    def lengthAfterTransformations(self, s, t):
        MOD = 10**9 + 7
        dp = [1] * 26
        for _ in range(t):
            new_dp = [0] * 26
            for j in range(25):
                new_dp[j] = dp[j+1]
            new_dp[25] = (dp[0] + dp[1]) % MOD
            dp = new_dp
        result = 0
        for ch in s:
            result = (result + dp[ord(ch) - ord('a')]) % MOD
        return result

print(Solution().lengthAfterTransformations("abcyy", 2)) 
print(Solution().lengthAfterTransformations("azbk", 1))   
