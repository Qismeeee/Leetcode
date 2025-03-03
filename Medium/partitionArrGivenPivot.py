class Solution(object):
    def pivotArray(self, nums, pivot):
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)
        return less_than_pivot + equal_to_pivot + greater_than_pivot


sol = Solution()

# Test Case 1
nums1 = [9, 12, 5, 10, 14, 3, 10]
pivot1 = 10
print("Test Case 1:")
print("Input: ", nums1, "Pivot:", pivot1)
print("Output:", sol.pivotArray(nums1, pivot1))

# Test Case 2
nums2 = [-3, 4, 3, 2]
pivot2 = 2
print("\nTest Case 2:")
print("Input: ", nums2, "Pivot:", pivot2)
print("Output:", sol.pivotArray(nums2, pivot2))

# Test Case 3
nums3 = [1, 2, 3, 4, 5, 6]
pivot3 = 3
print("\nTest Case 3:")
print("Input: ", nums3, "Pivot:", pivot3)
print("Output:", sol.pivotArray(nums3, pivot3))

# Test Case 4
nums4 = [5, 5, 5, 5, 5]
pivot4 = 5
print("\nTest Case 4:")
print("Input: ", nums4, "Pivot:", pivot4)
print("Output:", sol.pivotArray(nums4, pivot4))