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
    

def run_tests():
    solution = Solution()

    n1 = 5
    edges1 = [[0,1,7], [1,3,7], [1,2,1]]
    query1 = [[0,3], [3,4]]
    expected1 = [1, -1]
    result1 = solution.minimumCost(n1, edges1, query1)
    print("Test Case 1:", "Pass" if result1 == expected1 else f"Fail (Expected {expected1}, got {result1})")

    n2 = 3
    edges2 = [[0,2,7], [0,1,15], [1,2,6], [1,2,1]]
    query2 = [[1,2]]
    expected2 = [0]
    result2 = solution.minimumCost(n2, edges2, query2)
    print("Test Case 2:", "Pass" if result2 == expected2 else f"Fail (Expected {expected2}, got {result2})")

    n3 = 2
    edges3 = []
    query3 = [[0,1]]
    expected3 = [-1]
    result3 = solution.minimumCost(n3, edges3, query3)
    print("Test Case 3:", "Pass" if result3 == expected3 else f"Fail (Expected {expected3}, got {result3})")

    n4 = 2
    edges4 = [[0,1,5]]
    query4 = [[0,1], [1,0]]
    expected4 = [5, 5]
    result4 = solution.minimumCost(n4, edges4, query4)
    print("Test Case 4:", "Pass" if result4 == expected4 else f"Fail (Expected {expected4}, got {result4})")

if __name__ == "__main__":
    run_tests()
