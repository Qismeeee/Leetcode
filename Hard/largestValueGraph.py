from collections import deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)
        g = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            g[u].append(v)
            indegree[v] += 1
        dp = [[0] * 26 for _ in range(n)]
        q = deque(i for i in range(n) if indegree[i] == 0)
        count = 0
        res = 0
        while q:
            u = q.popleft()
            count += 1
            ci = ord(colors[u]) - 97
            dp[u][ci] += 1
            res = max(res, dp[u][ci])
            for v in g[u]:
                for c in range(26):
                    if dp[u][c] > dp[v][c]:
                        dp[v][c] = dp[u][c]
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return res if count == n else -1

tests = [
    ("abaca", [[0,1],[0,2],[2,3],[3,4]], 3),
    ("a", [[0,0]], -1),
    ("aaa", [[0,1],[1,2]], 3),
]

sol = Solution()
for colors, edges, expected in tests:
    result = sol.largestPathValue(colors, edges)
    print(result, expected)
    assert result == expected
