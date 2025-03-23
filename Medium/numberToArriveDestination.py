import heapq
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            cur_dist, node = heapq.heappop(heap)

            if cur_dist > dist[node]:
                continue

            for neighbor, time in graph[node]:
                new_dist = cur_dist + time
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (new_dist, neighbor))
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]


s = Solution()
n1 = 7
roads1 = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(s.countPaths(n1, roads1))  

n2 = 2
roads2 = [[1,0,10]]
print(s.countPaths(n2, roads2))  
