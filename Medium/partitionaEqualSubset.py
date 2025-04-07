class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
    
def test_canPartition():
    solution = Solution()

    nums1 = [1, 5, 11, 5]
    result1 = solution.canPartition(nums1)
    print(f"Test Case 1: {nums1} -> Result: {result1}")

    nums2 = [1, 2, 3, 5]
    result2 = solution.canPartition(nums2)
    print(f"Test Case 2: {nums2} -> Result: {result2}")

    nums3 = [2, 2, 2, 2, 2, 2]
    result3 = solution.canPartition(nums3)
    print(f"Test Case 3: {nums3} -> Result: {result3}")

    nums4 = [3, 34, 4, 12, 5, 2]
    result4 = solution.canPartition(nums4)
    print(f"Test Case 4: {nums4} -> Result: {result4}")

test_canPartition()