class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        
        return count

def test_solution():
    solution = Solution()

    # Test case 1
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
    expected = 4
    result = solution.countPairs(nums, k)
    assert result == expected, f"Test case 1 failed: expected {expected}, got {result}"

    # Test case 2
    nums = [1, 2, 3, 4]
    k = 1
    expected = 0
    result = solution.countPairs(nums, k)
    assert result == expected, f"Test case 2 failed: expected {expected}, got {result}"

    # Test case 3
    nums = [1, 1, 1, 1]
    k = 1
    expected = 6
    result = solution.countPairs(nums, k)
    assert result == expected, f"Test case 3 failed: expected {expected}, got {result}"

    # Test case 4
    nums = [5, 5, 5, 5, 5]
    k = 10
    expected = 10
    result = solution.countPairs(nums, k)
    assert result == expected, f"Test case 4 failed: expected {expected}, got {result}"

test_solution()
