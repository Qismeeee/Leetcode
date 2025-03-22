from collections import defaultdict, deque

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        complete_components = 0

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True
                nodes = [i] 
                edge_count = 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        edge_count += 1
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            nodes.append(neighbor)
                node_count = len(nodes)
                expected_edges = node_count * (node_count - 1) // 2

                if edge_count // 2 == expected_edges:
                    complete_components += 1

        return complete_components

s = Solution()

# Test case 1
n1 = 6
edges1 = [[0,1],[0,2],[1,2],[3,4]]
print(s.countCompleteComponents(n1, edges1))  

# Test case 2
n2 = 6
edges2 = [[0,1],[0,2],[1,2],[3,4],[3,5]]
print(s.countCompleteComponents(n2, edges2))  

# Test case 3
n3 = 4
edges3 = []
print(s.countCompleteComponents(n3, edges3))  

# Test case 4
n4 = 3
edges4 = [[0,1],[1,2]]
print(s.countCompleteComponents(n4, edges4))  

# Test case 5
n5 = 3
edges5 = [[0,1],[1,2],[0,2]]
print(s.countCompleteComponents(n5, edges5))  
