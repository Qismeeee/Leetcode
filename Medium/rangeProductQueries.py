class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        exps = []
        b = 0
        m = n
        while m:
            if m & 1:
                exps.append(b)
            m >>= 1
            b += 1
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)

        ans = []
        for l, r in queries:
            k = pref[r + 1] - pref[l]  
            ans.append(pow(2, k, MOD))
        return ans
