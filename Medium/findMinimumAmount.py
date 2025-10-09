class Solution(object):
    def minTime(self, skill, mana):
        n, m = len(skill), len(mana)
        A = [0]*(n+1)
        for i in range(1, n+1):
            A[i] = A[i-1] + skill[i-1]
        ans = mana[-1] * A[-1]
        for j in range(m-1):
            bj, bj1 = mana[j], mana[j+1]
            gap = 0
            for i in range(1, n+1):
                v = bj * A[i] - bj1 * A[i-1]
                if v > gap:
                    gap = v
            ans += gap
        return ans
