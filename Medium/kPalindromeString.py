from collections import Counter
import unittest

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        char_count = Counter(s)
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
        return k >= odd_count and k <= len(s)


class TestCanConstruct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_cases(self):
        self.assertTrue(self.solution.canConstruct("a", 1))  
        self.assertTrue(self.solution.canConstruct("aa", 1))  
        self.assertTrue(self.solution.canConstruct("abc", 3))  
        self.assertFalse(self.solution.canConstruct("abc", 2)) 
        self.assertTrue(self.solution.canConstruct("aabb", 1))  
if __name__ == "__main__":
    unittest.main()
