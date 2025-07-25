class Solution:
    def maxSum(self, nums: list[int]) -> int:
        max_value = max(nums)
        if all(n < 0 for n in nums):
            return max_value

        seen = [False] * 101
        for n in nums:
            if 0 <= n <= 100:
                seen[n] = True

        return sum(i for i, present in enumerate(seen[1:], start=1) if present)


def test_solution():
    sol = Solution()
    
    # Test case 1: Array with positive numbers
    nums1 = [1, 2, 3, 4, 5]
    result1 = sol.maxSum(nums1)
    print(f"Test 1: {nums1} -> {result1}")
    
    # Test case 2: Array with duplicates
    nums2 = [1, 1, 2, 2, 3]
    result2 = sol.maxSum(nums2)
    print(f"Test 2: {nums2} -> {result2}")
    
    # Test case 3: Array with all negative numbers
    nums3 = [-1, -2, -3]
    result3 = sol.maxSum(nums3)
    print(f"Test 3: {nums3} -> {result3}")
    
    # Test case 4: Mixed positive and negative
    nums4 = [1, -1, 2, -2, 3]
    result4 = sol.maxSum(nums4)
    print(f"Test 4: {nums4} -> {result4}")
    
    # Test case 5: With zero
    nums5 = [0, 1, 2, 3]
    result5 = sol.maxSum(nums5)
    print(f"Test 5: {nums5} -> {result5}")
    
    # Test case 6: Large numbers (> 100)
    nums6 = [1, 2, 150, 200]
    result6 = sol.maxSum(nums6)
    print(f"Test 6: {nums6} -> {result6}")
    
    # Test case 7: Single element
    nums7 = [5]
    result7 = sol.maxSum(nums7)
    print(f"Test 7: {nums7} -> {result7}")
    
    # Test case 8: Empty-like case with negative and large numbers
    nums8 = [-5, 150, -10, 200]
    result8 = sol.maxSum(nums8)
    print(f"Test 8: {nums8} -> {result8}")

test_solution()