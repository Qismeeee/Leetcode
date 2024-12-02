class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print("Test case 1: ", result)


nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print("Test case 2: ", result)

nums = [3, 3]
target = 6
result = solution.twoSum(nums, target)
print("Test case 3: ", result)