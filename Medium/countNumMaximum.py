class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num
        
        count = 0
        
        for mask in range(1, 1 << n):  
            current_or = 0
            for i in range(n):
                if mask & (1 << i):  
                    current_or |= nums[i]
            if current_or == max_or:
                count += 1
        
        return count
    
def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [3, 1]
    result1 = sol.countMaxOrSubsets(nums1)
    print(f"Example 1: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print(f"Max OR: {3 | 1} = 3")
    print(f"Subsets with max OR: [3], [3,1]")
    print()
    
    # Example 2
    nums2 = [2, 2, 2]
    result2 = sol.countMaxOrSubsets(nums2)
    print(f"Example 2: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 7")
    print(f"Max OR: {2 | 2 | 2} = 2")
    print(f"All non-empty subsets have OR = 2")
    print()
    
    # Example 3
    nums3 = [3, 2, 1, 5]
    result3 = sol.countMaxOrSubsets(nums3)
    print(f"Example 3: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 6")
    print(f"Max OR: {3 | 2 | 1 | 5} = 7")
    print()
    
    nums4 = [1]
    result4 = sol.countMaxOrSubsets(nums4)
    print(f"Test 4: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: 1")
    print()

def show_subsets_detail(nums):
    n = len(nums)
    max_or = 0
    for num in nums:
        max_or |= num
    
    print(f"Array: {nums}, Max possible OR: {max_or}")
    print("All subsets and their OR values:")
    
    for mask in range(1, 1 << n):
        subset = []
        current_or = 0
        
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
                current_or |= nums[i]
        
        marker = " ✓" if current_or == max_or else ""
        print(f"  {subset} -> OR = {current_or}{marker}")
    print()

test_solution()

print("=== Detailed breakdown for Example 1 ===")
show_subsets_detail([3, 1])