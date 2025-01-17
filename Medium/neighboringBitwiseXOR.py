class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        return xor_sum == 0

# Instantiate the solution class
solution = Solution()
derived_1 = [1, 1, 0]  
print(solution.doesValidArrayExist(derived_1))  

derived_2 = [1, 1]  
print(solution.doesValidArrayExist(derived_2))  

derived_3 = [1, 0]  
print(solution.doesValidArrayExist(derived_3))  

derived_4 = [0]  
print(solution.doesValidArrayExist(derived_4))  
derived_5 = [0, 0, 0, 0]  
print(solution.doesValidArrayExist(derived_5))  
