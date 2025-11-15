class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        m = len(zeros)
        if n == 0:
            return 0

        # Case z = 0: substrings toàn '1'
        ans = 0
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1

        if m == 0:
            return ans

        # Z^2 <= len <= n => Z <= sqrt(n)
        B = int(n ** 0.5)

        # Xử lý substring có đúng z số 0 (1 <= z <= B)
        for z in range(1, min(B, m) + 1):
            T = z * z + z  # len >= z^2 + z
            for p in range(m - z + 1):
                first = zeros[p]
                last = zeros[p + z - 1]

                prev_pos = zeros[p - 1] if p > 0 else -1
                next_pos = zeros[p + z] if p + z < m else n

                L_lo = prev_pos + 1
                L_hi = first
                R_lo = last
                R_hi = next_pos - 1

                if L_lo > L_hi or R_lo > R_hi:
                    continue

                C = R_hi - R_lo + 1  # số cách chọn r khi dùng R_lo

                # Vùng 1: l sao cho l + T - 1 <= R_lo  => l <= R_lo - T + 1
                if C > 0:
                    l1 = min(L_hi, R_lo - T + 1)
                else:
                    l1 = L_lo - 1

                if C > 0 and l1 >= L_lo:
                    ans += (l1 - L_lo + 1) * C

                # Vùng 2: l sao cho r = l + T - 1, và r <= R_hi
                # l >= R_lo - T + 2 và l <= R_hi - T + 1
                l2_start = max(L_lo, R_lo - T + 2)
                l2_end = min(L_hi, R_hi - T + 1)
                if l2_end >= l2_start:
                    n2 = l2_end - l2_start + 1
                    s0 = R_hi - T + 2 - l2_start
                    ans += n2 * s0 - n2 * (n2 - 1) // 2

        return ans
