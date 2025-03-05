class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return 2 * n * n - 2 * n + 1


print(Solution().coloredCells(1)) 
print(Solution().coloredCells(2))  
print(Solution().coloredCells(3))  
print(Solution().coloredCells(10)) 
print(Solution().coloredCells(1000)) 
print(Solution().coloredCells(100000)) 
print(Solution().coloredCells(100000))
print(Solution().coloredCells(99999))
print(Solution().coloredCells(100001))
print(Solution().coloredCells(1))
print(Solution().coloredCells(100000))