class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        nums = []
        for row in grid:
            nums.extend(row)
        expected_sum = (n * n * (n * n + 1)) // 2
        actual_sum = 0
        seen = set()
        repeated = -1
        
        for num in nums:
            if num in seen:
                repeated = num
            else:
                seen.add(num)
            actual_sum += num
        missing = expected_sum - actual_sum + repeated
        
        return [repeated, missing]

def test_findMissingAndRepeatedValues():
    solution = Solution()

    # Test case 1: grid = [[1,3],[2,2]]
    grid1 = [[1, 3], [2, 2]]
    result1 = solution.findMissingAndRepeatedValues(grid1)
    print(f"Test case 1: {result1}")  

    # Test case 2: grid = [[9,1,7], [8,9,2], [3,4,6]]
    grid2 = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    result2 = solution.findMissingAndRepeatedValues(grid2)
    print(f"Test case 2: {result2}") 

    # Test case 3: grid = [[1, 1]]
    grid3 = [[1, 1]]
    result3 = solution.findMissingAndRepeatedValues(grid3)
    print(f"Test case 3: {result3}") 


test_findMissingAndRepeatedValues()
