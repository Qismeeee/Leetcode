class Solution:
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10**9 + 7
        M = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                M[j][i] = 1
        def mat_mul(A, B):
            C = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    a = A[i][k]
                    if a:
                        for j in range(26):
                            C[i][j] = (C[i][j] + a * B[k][j]) % MOD
            return C

        def mat_pow(A, p):
            R = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base = A
            while p > 0:
                if p & 1:
                    R = mat_mul(R, base)
                base = mat_mul(base, base)
                p >>= 1
            return R

        Mt = mat_pow(M, t)
        v0 = [0] * 26
        for ch in s:
            v0[ord(ch) - ord('a')] += 1
        vt = [0] * 26
        for i in range(26):
            total = 0
            row = Mt[i]
            for j in range(26):
                total = (total + row[j] * v0[j]) % MOD
            vt[i] = total

        return sum(vt) % MOD
