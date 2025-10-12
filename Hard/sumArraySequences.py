MOD = 10**9 + 7

class Solution(object):
    def magicalSum(self, m, k, nums):
        n = len(nums)
        fact = [1]*(m+1)
        invfact = [1]*(m+1)
        for i in range(1, m+1):
            fact[i] = fact[i-1]*i % MOD
        invfact[m] = pow(fact[m], MOD-2, MOD)
        for i in range(m, 0, -1):
            invfact[i-1] = invfact[i]*i % MOD

        dp = [[[0]*(m+1) for _ in range(k+1)] for __ in range(m+1)]
        dp[0][0][0] = 1

        for v in nums:
            ndp = [[[0]*(m+1) for _ in range(k+1)] for __ in range(m+1)]
            powv = [1]*(m+1)
            for c in range(1, m+1):
                powv[c] = (powv[c-1]*v) % MOD
            for carry in range(m+1):
                for ones in range(k+1):
                    row = dp[carry][ones]
                    for used in range(m+1):
                        base = row[used]
                        if not base:
                            continue
                        maxc = m - used
                        for c in range(maxc+1):
                            nc = used + c
                            ncarry = (carry + c) >> 1
                            bit = (carry + c) & 1
                            nones = ones + bit
                            if nones > k:
                                continue
                            add = base * powv[c] % MOD * invfact[c] % MOD
                            ndp[ncarry][nones][nc] = (ndp[ncarry][nones][nc] + add) % MOD
            dp = ndp

        ans = 0
        for carry in range(m+1):
            pc = bin(carry).count("1")
            need = k - pc
            if 0 <= need <= k:
                ans = (ans + dp[carry][need][m]) % MOD
        ans = ans * fact[m] % MOD
        return ans

m = 2
k = 2
nums = [5,4,3,2,1]
s = Solution()
print(s.magicalSum(m, k, nums))
