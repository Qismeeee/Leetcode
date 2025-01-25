class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        sorted_indices = sorted(range(n), key=lambda x: nums[x])
        result = nums[:]
        current_group = []
        
        for i in range(n):
            if not current_group:
                current_group.append(sorted_indices[i])
            else:
                if abs(nums[sorted_indices[i]] - nums[sorted_indices[i-1]]) <= limit:
                    current_group.append(sorted_indices[i])
                else:
                    current_group_values = [nums[idx] for idx in current_group]
                    current_group_values.sort()
                    for idx, val in zip(sorted(current_group), current_group_values):
                        result[idx] = val
                    current_group = [sorted_indices[i]]
        
        if current_group:
            current_group_values = [nums[idx] for idx in current_group]
            current_group_values.sort()
            for idx, val in zip(sorted(current_group), current_group_values):
                result[idx] = val
        
        return result

# Test Case 1:
nums1 = [1, 5, 3, 9, 8]
limit1 = 2
solution = Solution()
print(solution.lexicographicallySmallestArray(nums1, limit1))  # Expected Output: [1, 3, 5, 8, 9]

# Test Case 2:
nums2 = [1, 7, 6, 18, 2, 1]
limit2 = 3
print(solution.lexicographicallySmallestArray(nums2, limit2))  # Expected Output: [1, 6, 7, 18, 1, 2]

# Test Case 3:
nums3 = [1, 7, 28, 19, 10]
limit3 = 3
print(solution.lexicographicallySmallestArray(nums3, limit3))  # Expected Output: [1, 7, 28, 19, 10]

# Test Case 4:
nums4 = [10, 20, 30, 40]
limit4 = 15
print(solution.lexicographicallySmallestArray(nums4, limit4))  # Expected Output: [10, 20, 30, 40]

# Test Case 5:
nums5 = [5, 5, 5, 5, 5]
limit5 = 0
print(solution.lexicographicallySmallestArray(nums5, limit5))  # Expected Output: [5, 5, 5, 5, 5]

# Test Case 6:
nums6 = [9, 1, 5, 7, 3]
limit6 = 5
print(solution.lexicographicallySmallestArray(nums6, limit6))  # Expected Output: [1, 5, 7, 9, 3]
