import math

class Solution(object):
    def idealArrays(self, n, maxValue):
        MOD = 10**9 + 7
        divisors = [[] for _ in range(maxValue + 1)]
        for d in range(1, maxValue + 1):
            for m in range(d * 2, maxValue + 1, d):
                divisors[m].append(d)
        maxLen = min(n, maxValue.bit_length())

        total_count = [0] * (maxLen + 1)
        count_prev = [1] * (maxValue + 1)
        total_count[1] = maxValue
        for length in range(2, maxLen + 1):
            count_curr = [0] * (maxValue + 1)
            for v in range(1, maxValue + 1):
                for d in divisors[v]:
                    count_curr[v] = (count_curr[v] + count_prev[d]) % MOD
            total_count[length] = sum(count_curr[1:]) % MOD
            count_prev = count_curr

        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i-1] * i % MOD
        invfac = [1] * (n + 1)
        invfac[n] = pow(fac[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfac[i-1] = invfac[i] * i % MOD
        result = 0
        for length in range(1, maxLen + 1):
            c = fac[n-1] * invfac[length-1] % MOD * invfac[n-length] % MOD
            result = (result + c * total_count[length]) % MOD
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (2, 5, 10),
        (5, 3, 11),
        (1, 100, 100),
        (3, 2, 4),
    ]
    for n, maxValue, expected in tests:
        result = sol.idealArrays(n, maxValue)
        print(n, maxValue, result, "OK" if result == expected else "WRONG")
