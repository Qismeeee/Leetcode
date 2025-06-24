class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        
        for i in range(n):
            is_k_distant = False
            for j in range(max(0, i - k), min(n, i + k + 1)):
                if nums[j] == key:
                    is_k_distant = True
                    break
            
            if is_k_distant:
                result.append(i)
        
        return result
    
def test_solution():
    sol = Solution()
    
    result1 = sol.findKDistantIndices([3,4,9,1,3,9,5], 9, 1)
    print(f"Example 1: {result1}")  
    result2 = sol.findKDistantIndices([2,2,2,2,2], 2, 2)
    print(f"Example 2: {result2}")  
    result3 = sol.findKDistantIndices([1,1,1,1], 2, 1)
    print(f"Test 3 (no key): {result3}")  
    result4 = sol.findKDistantIndices([5], 5, 0)
    print(f"Test 4 (single element): {result4}")  
test_solution()