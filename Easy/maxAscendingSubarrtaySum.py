class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        current_sum = 0
        
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        max_sum = max(max_sum, current_sum)  # to account for the last subarray
        return max_sum

solution = Solution()

# Test case 1
nums1 = [10, 20, 30, 5, 10, 50]
print(f"Test case 1: {nums1}, Max Ascending Sum: {solution.maxAscendingSum(nums1)}")

# Test case 2
nums2 = [10, 20, 30, 40, 50]
print(f"Test case 2: {nums2}, Max Ascending Sum: {solution.maxAscendingSum(nums2)}")

# Test case 3
nums3 = [12, 17, 15, 13, 10, 11, 12]
print(f"Test case 3: {nums3}, Max Ascending Sum: {solution.maxAscendingSum(nums3)}")

# Test case 4 (dùng một mảng có 1 phần tử)
nums4 = [5]
print(f"Test case 4: {nums4}, Max Ascending Sum: {solution.maxAscendingSum(nums4)}")

# Test case 5 (mảng có các phần tử giảm dần)
nums5 = [100, 90, 80, 70, 60]
print(f"Test case 5: {nums5}, Max Ascending Sum: {solution.maxAscendingSum(nums5)}")