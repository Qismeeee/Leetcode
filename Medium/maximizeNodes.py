from collections import deque
class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        n = max(max(u, v) for u, v in edges1) + 1
        m = max(max(u, v) for u, v in edges2) + 1
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(m)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        def bfs_count(g, size, limit):
            res = [0] * size
            for i in range(size):
                dist = [-1] * size
                q = deque([i])
                dist[i] = 0
                cnt = 0
                while q:
                    u = q.popleft()
                    if dist[u] <= limit:
                        cnt += 1
                        for w in g[u]:
                            if dist[w] < 0:
                                dist[w] = dist[u] + 1
                                q.append(w)
                res[i] = cnt
            return res
        cnt1 = bfs_count(g1, n, k)
        cnt2 = bfs_count(g2, m, k-1) if k > 0 else [0] * m
        best2 = max(cnt2) if k > 0 else 0
        return [cnt1[i] + best2 for i in range(n)]
