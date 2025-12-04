class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        from collections import defaultdict

        # Đếm số điểm trên từng hàng y
        cnt_y = defaultdict(int)
        for x, y in points:
            cnt_y[y] += 1

        inv2 = (MOD + 1) // 2  # nghịch đảo của 2 mod MOD
        S1 = 0  # sum of C(ci, 2)
        S2 = 0  # sum of C(ci, 2)^2

        for c in cnt_y.values():
            if c >= 2:
                # Ai = C(c, 2) = c*(c-1)/2
                Ai = c * (c - 1) // 2
                Ai_mod = Ai % MOD
                S1 = (S1 + Ai_mod) % MOD
                S2 = (S2 + Ai_mod * Ai_mod) % MOD

        # Tổng số hình thang ngang:
        # Σ_{i<j} Ai * Aj = ((Σ Ai)^2 - Σ Ai^2)/2
        ans = (S1 * S1 - S2) % MOD
        ans = ans * inv2 % MOD
        return ans
