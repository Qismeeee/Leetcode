class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):
            if nums[i] == 0:  
                operations += 1
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
        
        if all(x == 1 for x in nums):
            return operations
        else:
            return -1


def test_solution():
    solution = Solution()
    
    test_cases = [
        ([0,1,1,1,0,0], 3),  
        ([0,1,1,1], -1),      
        ([0,0,0,0,0,0], 2), 
        ([1,1,1,1,1], 0),     
        ([0,0,1,0,0,1,0,0,1], 3),  
        ([0,0,0], 1),         
        ([1,0,0,0,1,1,0,0,0,1], 3),  
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.minOperations(nums[:])  
        print(f"Test Case {i+1}: {'Pass' if result == expected else 'Fail'} (Output: {result}, Expected: {expected})")

test_solution()
