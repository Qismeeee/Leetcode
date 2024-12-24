from collections import defaultdict, deque

class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def tree_diameter(edges, n):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            def bfs(start):
                visited = [-1] * n
                visited[start] = 0
                q = deque([start])
                farthest_node = start
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if visited[neighbor] == -1:
                            visited[neighbor] = visited[node] + 1
                            q.append(neighbor)
                            farthest_node = neighbor
                return farthest_node, visited[farthest_node]
            
            node_u, _ = bfs(0)
            node_v, diameter = bfs(node_u)
            return diameter, (node_u, node_v)
        
        def half_diameter(diameter):
            return (diameter + 1) // 2  
        
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        
        d1, _ = tree_diameter(edges1, n1)
        d2, _ = tree_diameter(edges2, n2)
        result = max(d1, d2, half_diameter(d1) + half_diameter(d2) + 1)
        return result

edges1 = [[0, 1]]
edges2 = [[0, 1]]
sol = Solution()
print(sol.minimumDiameterAfterMerge(edges1, edges2))
