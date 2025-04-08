class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if len(set(nums)) == n:
            return 0
        
        operations = 0
        while True:
            if len(set(nums)) == len(nums):
                return operations
            if len(nums) <= 3:
                nums = []
                operations += 1
                return operations
            else:
                nums = nums[3:]
                operations += 1

def test_minimumOperations():
    solution = Solution()
    nums1 = [1, 2, 3, 4, 2, 3, 3, 5, 7]
    result1 = solution.minimumOperations(nums1)
    print(f"Test Case 1: {nums1} -> Result: {result1}")  

    nums2 = [4, 5, 6, 4, 4]
    result2 = solution.minimumOperations(nums2)
    print(f"Test Case 2: {nums2} -> Result: {result2}")  

    nums3 = [6, 7, 8, 9]
    result3 = solution.minimumOperations(nums3)
    print(f"Test Case 3: {nums3} -> Result: {result3}")

    nums4 = [1, 1, 1, 1, 1]
    result4 = solution.minimumOperations(nums4)
    print(f"Test Case 4: {nums4} -> Result: {result4}") 

    nums5 = [10, 20, 30, 40]
    result5 = solution.minimumOperations(nums5)
    print(f"Test Case 5: {nums5} -> Result: {result5}") 

test_minimumOperations()
