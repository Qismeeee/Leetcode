class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for a, b in zip(s1, s2):
            union(a, b)

        return ''.join(find(c) for c in baseStr)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s1 = "parker"
        s2 = "morris"
        baseStr = "parser"
        expected = "makkek"
        result = self.sol.smallestEquivalentString(s1, s2, baseStr)
        self.assertEqual(result, expected)

    def test_case2(self):
        s1 = "hello"
        s2 = "world"
        baseStr = "hold"
        expected = "hdld"
        result = self.sol.smallestEquivalentString(s1, s2, baseStr)
        self.assertEqual(result, expected)

    def test_case3(self):
        s1 = "leetcode"
        s2 = "programs"
        baseStr = "sourcecode"
        expected = "aauaaaaada"
        result = self.sol.smallestEquivalentString(s1, s2, baseStr)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
