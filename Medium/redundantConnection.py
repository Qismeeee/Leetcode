import unittest

class Solution(object):
    def findRedundantConnection(self, edges):
        """
      :type edges: List[List[int]]
      :rtype: List[int]
        """
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(n):
            p = parent[n]
            while p!= parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
class TestFindRedundantConnection(unittest.TestCase):

    def test_example_1(self):
        edges = [[1,2],[1,3],[2,3]]
        expected = [2,3]
        self.assertEqual(Solution().findRedundantConnection(edges), expected)

    def test_example_2(self):
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        expected = [1,4]
        self.assertEqual(Solution().findRedundantConnection(edges), expected)

    def test_simple_case(self):
        edges = [[1,2],[1,3],[1,4],[3,4]]
        expected = [3,4]
        self.assertEqual(Solution().findRedundantConnection(edges), expected)

if __name__ == '__main__':
    unittest.main()