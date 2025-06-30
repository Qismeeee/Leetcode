class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(nums)
        max_length = 0
        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])
        
        return max_length

def test_solution():
    sol = Solution()
    
    result1 = sol.findLHS([1,3,2,2,5,2,3,7])
    print(f"Example 1: {result1}")  
    
    result2 = sol.findLHS([1,2,3,4])
    print(f"Example 2: {result2}")  
    
    result3 = sol.findLHS([1,1,1,1])
    print(f"Example 3: {result3}")  
    print(f"Empty array: {sol.findLHS([])}")  
    print(f"Single element: {sol.findLHS([5])}")  
    print(f"Two same: {sol.findLHS([1,1])}") 
    print(f"Two consecutive: {sol.findLHS([1,2])}")  

test_solution()