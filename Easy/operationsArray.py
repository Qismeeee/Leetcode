class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        for i in range(n - 1):  
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        non_zero_elements = [num for num in nums if num != 0]
        zero_count = n - len(non_zero_elements)
        non_zero_elements.extend([0] * zero_count)
        
        return non_zero_elements

solution = Solution()

# Test Case 1: Simple case, no adjacent equal numbers
print(solution.applyOperations([1, 2, 2, 1, 1, 0])) 

# Test Case 2: Array with a 0 and no operations applied
print(solution.applyOperations([0, 1])) 

# Test Case 3: All elements are equal
print(solution.applyOperations([2, 2, 2, 2])) 

# Test Case 4: No equal adjacent elements
print(solution.applyOperations([1, 3, 5, 7]))  

# Test Case 5: Only zeros in the array
print(solution.applyOperations([0, 0, 0, 0])) 

# Test Case 6: Array with a single element
print(solution.applyOperations([5]))