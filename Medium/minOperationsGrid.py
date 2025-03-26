class Solution(object):
    def minOperations(self, grid, x):
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1  
        
        nums.sort()
        median = nums[len(nums) // 2]
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations
    
def test_minOperations():
   solution = Solution()
   
   # Test case 1
   grid1 = [[2,4],[6,8]]
   x1 = 2
   result1 = solution.minOperations(grid1, x1)
   print(f"Test case 1: {result1}")  
   
   # Test case 2
   grid2 = [[1,5],[2,3]]
   x2 = 1
   result2 = solution.minOperations(grid2, x2)
   print(f"Test case 2: {result2}")  
   
   # Test case 3
   grid3 = [[1,2],[3,4]]
   x3 = 2
   result3 = solution.minOperations(grid3, x3)
   print(f"Test case 3: {result3}")  
   
   # Custom test case 4
   grid4 = [[1,3,5],[7,9,11]]
   x4 = 2
   result4 = solution.minOperations(grid4, x4)
   print(f"Test case 4: {result4}") 
   
   # Custom test case 5
   grid5 = [[10,10],[10,10]]
   x5 = 3
   result5 = solution.minOperations(grid5, x5)
   print(f"Test case 5: {result5}")  

class Solution(object):
   def minOperations(self, grid, x):
       nums = []
       for row in grid:
           for num in row:
               nums.append(num)
       
       remainder = nums[0] % x
       for num in nums:
           if num % x != remainder:
               return -1
       
       nums.sort()
       median = nums[len(nums) // 2]
       
       operations = 0
       for num in nums:
           operations += abs(num - median) // x
       
       return operations

if __name__ == "__main__":
   test_minOperations()