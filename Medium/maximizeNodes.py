from collections import deque
import unittest

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


class TestMaxTargetNodes(unittest.TestCase):
    def test_example1(self):
        edges1 = [[0,1],[0,2],[2,3],[2,4]]
        edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
        self.assertEqual(Solution().maxTargetNodes(edges1, edges2, 2), [9,7,9,8,8])
    def test_example2(self):
        edges1 = [[0,1],[0,2],[0,3],[0,4]]
        edges2 = [[0,1],[1,2],[2,3]]
        self.assertEqual(Solution().maxTargetNodes(edges1, edges2, 1), [6,3,3,3,3])

if __name__ == "__main__":
    unittest.main()
