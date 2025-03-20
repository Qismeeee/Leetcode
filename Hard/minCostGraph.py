class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        parent = list(range(n))
        rank = [0] * n
        component_and = [-1] * n 

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True

        for u, v, w in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                component_and[root_u] &= w
            else:
                union(u, v)
                new_root = find(u)  
                component_and[new_root] = component_and[root_u] & component_and[root_v] & w

        answer = []
        for si, ti in query:
            root_si = find(si)
            root_ti = find(ti)
            if root_si == root_ti:
                answer.append(component_and[root_si])
            else:
                answer.append(-1)

        return answer