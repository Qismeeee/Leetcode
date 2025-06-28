class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        selected = indexed_nums[:k]
        selected.sort(key=lambda x: x[1])
        result = [value for value, index in selected]
        return result
    
def test_solution():
    sol = Solution()
    
    result1 = sol.maxSubsequence([2,1,3,3], 2)
    print(f"Example 1: {result1}")  
    result2 = sol.maxSubsequence([-1,-2,3,4], 3)
    print(f"Example 2: {result2}")  
    result3 = sol.maxSubsequence([3,4,3,3], 2)
    print(f"Example 3: {result3}") 
    nums = [-1,-2,3,4]
    k = 3
    print(f"\nTracing Example 2: nums={nums}, k={k}")
    
    # Step 1: Create indexed pairs
    indexed_nums = [(nums[i], i) for i in range(len(nums))]
    print(f"Indexed pairs: {indexed_nums}")
    
    # Step 2: Sort by value descending
    indexed_nums.sort(key=lambda x: x[0], reverse=True)
    print(f"Sorted by value (desc): {indexed_nums}")
    
    # Step 3: Take k largest
    selected = indexed_nums[:k]
    print(f"Selected k={k} largest: {selected}")
    
    # Step 4: Sort by original index
    selected.sort(key=lambda x: x[1])
    print(f"Sorted by original index: {selected}")
    
    # Step 5: Extract values
    result = [value for value, index in selected]
    print(f"Final result: {result}")
    print(f"Sum: {sum(result)}")

    print(f"\nAdditional tests:")
    print(f"maxSubsequence([1], 1): {sol.maxSubsequence([1], 1)}")
    print(f"maxSubsequence([1,2,3,4,5], 3): {sol.maxSubsequence([1,2,3,4,5], 3)}")
    print(f"maxSubsequence([5,4,3,2,1], 3): {sol.maxSubsequence([5,4,3,2,1], 3)}")

test_solution()