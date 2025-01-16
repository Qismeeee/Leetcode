class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor_result = 0
        if len(nums2) % 2 == 1:
            for num in nums1:
                xor_result ^= num
        if len(nums1) % 2 == 1:
            for num in nums2:
                xor_result ^= num

        return xor_result

def test_solution():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 1, 3]
    nums2 = [10, 2, 5, 0]
    print("Test Case 1 Output:", solution.xorAllNums(nums1, nums2))  # Expected: 13
    
    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Test Case 2 Output:", solution.xorAllNums(nums1, nums2))  # Expected: 0
    
    # Test case 3: Single element in each array
    nums1 = [7]
    nums2 = [8]
    print("Test Case 3 Output:", solution.xorAllNums(nums1, nums2))  # Expected: 15
    
    # Test case 4: Large arrays with even length
    nums1 = [i for i in range(1000)]
    nums2 = [j for j in range(1000)]
    print("Test Case 4 Output:", solution.xorAllNums(nums1, nums2))  # Expected: 0
    
    # Test case 5: Large arrays with odd length
    nums1 = [i for i in range(1001)]
    nums2 = [j for j in range(1001)]
    print("Test Case 5 Output:", solution.xorAllNums(nums1, nums2))  # Expected: Depends on the array contents

test_solution()