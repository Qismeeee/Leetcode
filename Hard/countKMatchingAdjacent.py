MOD = 10**9 + 7

class Solution(object):
    def countGoodArrays(self, n, m, k):
        c = n - 1 - k
        if c < 0:
            return 0
        fact = [1] * (n)
        for i in range(1, n):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (n)
        invfact[-1] = pow(fact[-1], MOD-2, MOD)
        for i in range(n-1, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        comb = fact[n-1] * invfact[c] % MOD * invfact[n-1-c] % MOD
        return m * comb % MOD * pow(m-1, c, MOD) % MOD
    
if __name__ == "__main__":
    tests = [
        (3, 2, 1, 4),
        (4, 2, 2, 6),
        (5, 2, 0, 2),
        (6, 3, 2, 3 *  C(5, 3) * 2**3 % MOD),  
        (1, 10, 0, 10),
    ]
    for n, m, k, expected in tests:
        result = Solution().countGoodArrays(n, m, k)
        status = 'PASS' if result == expected else 'FAIL'
        print(f"n={n}, m={m}, k={k} -> {result} (expected {expected}) {status}")