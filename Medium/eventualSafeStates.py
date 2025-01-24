class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        visited = [0] * n  # 0: unvisited, 1: safe, -1: unsafe
        
        def dfs(node):
            if visited[node] != 0:
                return visited[node]
            
            visited[node] = -1  
            for neighbor in graph[node]:
                if dfs(neighbor) == -1:  
                    return -1
            visited[node] = 1 
            return 1
        
        safe_nodes = []
        for i in range(n):
            if dfs(i) == 1: 
                safe_nodes.append(i)
        
        return safe_nodes
