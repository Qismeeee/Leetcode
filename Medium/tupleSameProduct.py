import unittest

class Solution(object):
    def tupleSameProduct(self, nums):
        """
      :type nums: List[int]
      :rtype: int
        """
        from collections import defaultdict

        n = len(nums)
        product_count = defaultdict(int)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        for product, count in product_count.items():
            if count > 1:
                result += count * (count - 1) * 4  

        return result
    
class TestTupleSameProduct(unittest.TestCase):

    def test_empty_array(self):
        nums = []
        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), 0)

    def test_example_1(self):
        nums = [2, 3, 4, 6]
        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), 8)

    def test_example_2(self):
        nums = [1, 2, 4, 5, 10]
        solution = Solution()
        self.assertEqual(solution.tupleSameProduct(nums), 16)

if __name__ == '__main__':
    unittest.main()