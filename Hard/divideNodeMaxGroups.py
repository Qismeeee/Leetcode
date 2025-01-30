import unittest
from collections import deque
class Solution(object):
    def magnificentSets(self, n, edges):
        graph = [[] for _ in range(n)]

        for start, end in edges:
            graph[start - 1].append(end - 1)
            graph[end - 1].append(start - 1)

        distances = [0] * n

        for i in range(n):
            queue = deque([i])
            distance_map = [0] * n
            distance_map[i] = 1
            max_dist = 1
            root_node = i

            while queue:
                current_node = queue.popleft()
                root_node = min(root_node, current_node)

                for neighbor in graph[current_node]:
                    if distance_map[neighbor] == 0:
                        distance_map[neighbor] = distance_map[current_node] + 1
                        max_dist = max(max_dist, distance_map[neighbor])
                        queue.append(neighbor)
                    elif abs(distance_map[neighbor] - distance_map[current_node]) != 1:
                        return -1

            distances[root_node] = max(distances[root_node], max_dist)

        return sum(distances)
    
class TestMagnificentSets(unittest.TestCase):

    def test_simple_tree(self):
        sol = Solution()
        n = 5
        edges = [[1, 2], [1, 3], [2, 4], [2, 5]]
        self.assertEqual(sol.magnificentSets(n, edges), 3)

    def test_graph_with_cycle(self):
        sol = Solution()
        n = 4
        edges = [[1, 2], [2, 3], [3, 4], [4, 1]]
        self.assertEqual(sol.magnificentSets(n, edges), -1)

    def test_disconnected_graph(self):
        sol = Solution()
        n = 6
        edges = [[1, 2], [3, 4]]
        self.assertEqual(sol.magnificentSets(n, edges), 4)

    def test_single_node(self):
        sol = Solution()
        n = 1
        edges = []
        self.assertEqual(sol.magnificentSets(n, edges), 1)

if __name__ == '__main__':
    unittest.main()