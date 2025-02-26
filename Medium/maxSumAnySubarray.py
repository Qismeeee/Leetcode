import unittest

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        min_so_far = 0
        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(0, current_max + num)
            max_so_far = max(max_so_far, current_max)
            current_min = min(0, current_min + num)
            min_so_far = min(min_so_far, current_min)

        return max(abs(max_so_far), abs(min_so_far))
    

class TestSolution(unittest.TestCase):

    def test_example1(self):
        solution = Solution()
        nums = [1, -3, 2, 3, -4]
        self.assertEqual(solution.maxAbsoluteSum(nums), 5)

    def test_example2(self):
        solution = Solution()
        nums = [2, -5, 1, -4, 3, -2]
        self.assertEqual(solution.maxAbsoluteSum(nums), 8)

    def test_all_positive(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(solution.maxAbsoluteSum(nums), 15)

    def test_all_negative(self):
        solution = Solution()
        nums = [-1, -2, -3, -4, -5]
        self.assertEqual(solution.maxAbsoluteSum(nums), 15)

    def test_single_element_positive(self):
        solution = Solution()
        nums = [10]
        self.assertEqual(solution.maxAbsoluteSum(nums), 10)

    def test_single_element_negative(self):
        solution = Solution()
        nums = [-10]
        self.assertEqual(solution.maxAbsoluteSum(nums), 10)

    def test_empty_subarray(self):
         solution = Solution()
         nums = [0,0,0,0]
         self.assertEqual(solution.maxAbsoluteSum(nums), 0)

    def test_mixed_large_numbers(self):
        solution = Solution()
        nums = [-10000, 5000, -3000, 8000]
        self.assertEqual(solution.maxAbsoluteSum(nums), 10000)

    def test_long_mixed(self):
        solution = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(solution.maxAbsoluteSum(nums), 6)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)