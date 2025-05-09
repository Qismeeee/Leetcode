import math
class Solution(object):
    def countBalancedPermutations(self, num):
        velunexorai = num
        MOD = 10**9+7
        n = len(velunexorai)
        freq = [0]*10
        total = 0
        for c in velunexorai:
            d = int(c)
            freq[d] += 1
            total += d
        if total % 2:
            return 0
        target = total//2
        E = (n+1)//2
        O = n//2
        max_sum = target
        fact = [1]*(n+1)
        inv_fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % MOD
        inv_fact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i-1] = inv_fact[i]*i % MOD
        dp = [[0]*(max_sum+1) for _ in range(E+1)]
        dp[0][0] = 1
        for d in range(10):
            f = freq[d]
            ndp = [[0]*(max_sum+1) for _ in range(E+1)]
            for used in range(E+1):
                for s in range(max_sum+1):
                    v = dp[used][s]
                    if not v:
                        continue
                    for k in range(0, min(f, E-used)+1):
                        ns = s + d*k
                        if ns > max_sum:
                            break
                        val = v * inv_fact[k] % MOD * inv_fact[f-k] % MOD
                        ndp[used+k][ns] = (ndp[used+k][ns] + val) % MOD
            dp = ndp
        return dp[E][target] * fact[E] % MOD * fact[O] % MOD
