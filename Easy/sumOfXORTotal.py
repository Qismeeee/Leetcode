class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        for i in range(1 << n): 
            xor_sum = 0
            for j in range(n):
                if i & (1 << j):
                    xor_sum ^= nums[j]
            total_sum += xor_sum
        return total_sum


def test_subsetXORSum():
    solution = Solution()
    nums1 = [1, 3]
    result1 = solution.subsetXORSum(nums1)
    print(f"Test Case 1: {nums1} -> Result: {result1}")  

    nums2 = [5, 1, 6]
    result2 = solution.subsetXORSum(nums2)
    print(f"Test Case 2: {nums2} -> Result: {result2}")  

    nums3 = [3, 4, 5, 6, 7, 8]
    result3 = solution.subsetXORSum(nums3)
    print(f"Test Case 3: {nums3} -> Result: {result3}") 

test_subsetXORSum()
