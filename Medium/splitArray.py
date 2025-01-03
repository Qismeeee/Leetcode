class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        prefix_sum = 0
        valid_splits = 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i] 
            suffix_sum = total_sum - prefix_sum
            
            if prefix_sum >= suffix_sum:
                valid_splits += 1
        
        return valid_splits

def test_waysToSplitArray():
    solution = Solution()
    # Test case 1
    nums = [10, 4, -8, 7]
    expected = 2
    result = solution.waysToSplitArray(nums)
    print(f"Test case 1: {'Passed' if result == expected else 'Failed'} - Output: {result}")
    # Test case 2
    nums = [2, 3, 1, 0]
    expected = 2
    result = solution.waysToSplitArray(nums)
    print(f"Test case 2: {'Passed' if result == expected else 'Failed'} - Output: {result}")
    # Test case 3: Single large number followed by zeros
    nums = [100000, 0, 0, 0]
    expected = 3
    result = solution.waysToSplitArray(nums)
    print(f"Test case 3: {'Passed' if result == expected else 'Failed'} - Output: {result}")
    # Test case 4: All elements are equal
    nums = [5, 5, 5, 5]
    expected = 3
    result = solution.waysToSplitArray(nums)
    print(f"Test case 4: {'Passed' if result == expected else 'Failed'} - Output: {result}")
    # Test case 5: Alternating positive and negative numbers
    nums = [1, -1, 2, -2, 3, -3]
    expected = 1
    result = solution.waysToSplitArray(nums)
    print(f"Test case 5: {'Passed' if result == expected else 'Failed'} - Output: {result}")
    # Test case 6: Only two elements
    nums = [1, 1]
    expected = 1
    result = solution.waysToSplitArray(nums)
    print(f"Test case 6: {'Passed' if result == expected else 'Failed'} - Output: {result}")

test_waysToSplitArray()
