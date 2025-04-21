class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        sum, maxi, mini = 0, 0, 0
        for x in differences:
            sum += x
            maxi = max(maxi, sum)
            mini = min(mini, sum)
        return max(0, upper - lower - maxi + mini + 1)
    

sol = Solution()
# Test case 1
print(sol.numberOfArrays([1, -3, 4], 1, 6)) 
# Test case 2
print(sol.numberOfArrays([3, -4, 5, 1, -2], -4, 5))  
# Test case 3
print(sol.numberOfArrays([4, -7, 2], 3, 6))  
# Test case 4
print(sol.numberOfArrays([1, 1, 1], 1, 5)) 
# Test case 5
print(sol.numberOfArrays([-1, -1, -1], -5, 0))