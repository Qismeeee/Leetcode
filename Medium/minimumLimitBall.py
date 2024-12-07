class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDivide(penalty):
            operations = 0
            for balls in nums:
                operations += (balls - 1) // penalty
                if operations > maxOperations:
                    return False
            return True

        low, high = 1, max(nums)
        result = high
        while low <= high:
            mid = (low + high) // 2
            if canDivide(mid):
                result = mid  
                high = mid - 1
            else:
                low = mid + 1
        return result


solution = Solution()

# Test Case 1
nums = [9]
maxOperations = 2
print(solution.minimumSize(nums, maxOperations))

# Test Case 2
nums = [2, 4, 8, 2]
maxOperations = 4
print(solution.minimumSize(nums, maxOperations))  

# Test Case 3
nums = [7, 17, 3, 12]
maxOperations = 7
print(solution.minimumSize(nums, maxOperations)) 

# Test Case 4
nums = [1, 10, 10, 10]
maxOperations = 5
print(solution.minimumSize(nums, maxOperations)) 

# Test Case 5
nums = [1]
maxOperations = 1
print(solution.minimumSize(nums, maxOperations))  