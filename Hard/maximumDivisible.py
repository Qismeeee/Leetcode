import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        # Build adjacency list
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        self.ans = 0

        def dfs(u, p):
            # sum of subtree u modulo k
            total = values[u] % k
            for v in g[u]:
                if v == p:
                    continue
                total = (total + dfs(v, u)) % k

            # If subtree sum is divisible by k, this can be a component
            if total % k == 0:
                self.ans += 1
                return 0
            return total

        dfs(0, -1)
        return self.ans
