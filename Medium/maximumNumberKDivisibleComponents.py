from collections import defaultdict

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        components = [0]
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            subtree_sum = values[node]

            for neighbor in tree[node]:
                if not visited[neighbor]:
                    child_sum = dfs(neighbor)
                    if child_sum % k == 0:
                        components[0] += 1
                    else:
                        subtree_sum += child_sum
            
            return subtree_sum

        total_sum = dfs(0)
        if total_sum % k == 0:
            components[0] += 1

        return components[0]

n = 5
edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
values = [1, 8, 1, 4, 4]
k = 6

solution = Solution()
result = solution.maxKDivisibleComponents(n, edges, values, k)
print(result) 