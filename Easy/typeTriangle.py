class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"


sol = Solution()
print(sol.triangleType([3, 3, 3]))  
print(sol.triangleType([3, 4, 5])) 
print(sol.triangleType([1, 2, 3]))  
print(sol.triangleType([5, 5, 3]))  
