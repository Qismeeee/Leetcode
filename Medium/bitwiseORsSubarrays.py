class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        all_ors = set()
        current_ors = set()
        
        for num in arr:
            new_ors = set()
            new_ors.add(num)
            for prev_or in current_ors:
                new_ors.add(prev_or | num)
            current_ors = new_ors
            all_ors.update(current_ors)
        
        return len(all_ors)

class SolutionOptimized(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        all_ors = set()
        current_ors = set()
        
        for num in arr:
            current_ors = {num} | {prev_or | num for prev_or in current_ors}
            all_ors.update(current_ors)
        
        return len(all_ors)

def test_solution():
    sol = Solution()
    sol_opt = SolutionOptimized()
    
    # Example 1
    arr1 = [0]
    result1 = sol.subarrayBitwiseORs(arr1)
    result1_opt = sol_opt.subarrayBitwiseORs(arr1)
    print(f"Example 1: {arr1}")
    print(f"Output: {result1} (Optimized: {result1_opt})")
    print(f"Expected: 1")
    print(f"Subarrays: [0] -> OR values: {0}")
    print()
    
    # Example 2
    arr2 = [1, 1, 2]
    result2 = sol.subarrayBitwiseORs(arr2)
    result2_opt = sol_opt.subarrayBitwiseORs(arr2)
    print(f"Example 2: {arr2}")
    print(f"Output: {result2} (Optimized: {result2_opt})")
    print(f"Expected: 3")
    print("Subarrays and their OR values:")
    print("  [1] -> 1")
    print("  [1] -> 1") 
    print("  [2] -> 2")
    print("  [1,1] -> 1")
    print("  [1,2] -> 3")
    print("  [1,1,2] -> 3")
    print("Unique OR values: {1, 2, 3}")
    print()
    
    # Example 3
    arr3 = [1, 2, 4]
    result3 = sol.subarrayBitwiseORs(arr3)
    result3_opt = sol_opt.subarrayBitwiseORs(arr3)
    print(f"Example 3: {arr3}")
    print(f"Output: {result3} (Optimized: {result3_opt})")
    print(f"Expected: 6")
    print("Subarrays and their OR values:")
    print("  [1] -> 1")
    print("  [2] -> 2")
    print("  [4] -> 4")
    print("  [1,2] -> 3")
    print("  [2,4] -> 6")
    print("  [1,2,4] -> 7")
    print("Unique OR values: {1, 2, 3, 4, 6, 7}")
    print()
    
    arr4 = [1, 4, 2, 8]
    result4 = sol.subarrayBitwiseORs(arr4)
    result4_opt = sol_opt.subarrayBitwiseORs(arr4)
    print(f"Test 4: {arr4}")
    print(f"Output: {result4} (Optimized: {result4_opt})")
    print()

def trace_algorithm(arr):
    print(f"=== Tracing algorithm for {arr} ===")
    all_ors = set()
    current_ors = set()
    
    for i, num in enumerate(arr):
        print(f"Step {i + 1}: Processing arr[{i}] = {num}")
        print(f"  Previous OR values ending at position {i - 1}: {current_ors}")
        
        new_ors = {num}
        for prev_or in current_ors:
            new_or = prev_or | num
            new_ors.add(new_or)
            print(f"    {prev_or} | {num} = {new_or}")
        
        current_ors = new_ors
        all_ors.update(current_ors)
        
        print(f"  OR values ending at position {i}: {current_ors}")
        print(f"  All unique OR values so far: {sorted(all_ors)}")
        print()
    
    print(f"Final result: {len(all_ors)} unique OR values")
    return len(all_ors)

test_solution()
trace_algorithm([1, 1, 2])