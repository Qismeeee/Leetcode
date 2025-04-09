class Solution(object):
    def minOperations(self, nums, k):
        if len(nums) < 2:
            return -1
        nums.sort(reverse=True)
        operations = 0
        while nums and nums[0] > k:
            h = nums[0]
            nums = [min(num, h) for num in nums]
            operations += 1
            nums = [num for num in nums if num != h]
        if all(num == k for num in nums):
            return operations
        else:
            return -1

test_cases = [
    ([5, 2, 5, 4, 5], 2),  
    ([2, 1, 2], 2),  
    ([9, 7, 5, 3], 1),   
    ([10, 20, 10], 10),    
    ([1, 2, 3, 4, 5], 1),  
    ([3, 3, 3], 3),        
]

for nums, k in test_cases:
    print(f"nums = {nums}, k = {k} => Operations: {Solution().minOperations(nums, k)}")
