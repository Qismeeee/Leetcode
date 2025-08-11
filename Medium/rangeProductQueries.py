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

def run_tests():
    sol = Solution()
    cases = [
        (15, [[0,1],[2,2],[0,3]], [2,4,64]),
        (2, [[0,0]], [2]),
        (1, [[0,0]], [1]),
        (10, [[0,0],[1,1],[0,1]], [2,8,16]),
        (37, [[0,0],[1,2],[0,2]], [1,128,128]),
    ]
    for n, qs, expected in cases:
        got = sol.productQueries(n, qs)
        assert got == expected, (n, qs, expected, got)
    print("OK")

run_tests()
