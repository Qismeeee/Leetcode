class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n):
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] < lower:
                    left = mid + 1
                elif nums[i] + nums[mid] > upper:
                    right = mid - 1
                else:
                    count += (right - mid + 1)
                    break
        
        return count


def test_solution():
    solution = Solution()

    # Test case 1
    nums = [3,1,2,2,2,1,3]
    lower = 3
    upper = 6
    expected = 6
    result = solution.countFairPairs(nums, lower, upper)
    assert result == expected, f"Test case 1 failed: expected {expected}, got {result}"

    # Test case 2
    nums = [1,7,9,2,5]
    lower = 11
    upper = 11
    expected = 1
    result = solution.countFairPairs(nums, lower, upper)
    assert result == expected, f"Test case 2 failed: expected {expected}, got {result}"

    # Test case 3
    nums = [1, 1, 1, 1]
    lower = 2
    upper = 4
    expected = 6
    result = solution.countFairPairs(nums, lower, upper)
    assert result == expected, f"Test case 3 failed: expected {expected}, got {result}"

    # Test case 4
    nums = [1, 2, 3, 4, 5]
    lower = 10
    upper = 12
    expected = 0
    result = solution.countFairPairs(nums, lower, upper)
    assert result == expected, f"Test case 4 failed: expected {expected}, got {result}"

    print("All test cases passed!")

test_solution()
