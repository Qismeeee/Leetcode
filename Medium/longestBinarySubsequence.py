class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        zeros = s.count('0')
        value = 0
        ones_count = 0
        bit_position = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                if value + (1 << bit_position) <= k:
                    value += (1 << bit_position)
                    ones_count += 1
            bit_position += 1
        
        return zeros + ones_count

def test_solution():
    sol = Solution()
    
    # Example 1
    result1 = sol.longestSubsequence("1001010", 5)
    print(f"Example 1: {result1}") 
    # Example 2
    result2 = sol.longestSubsequence("00101001", 1)
    print(f"Example 2: {result2}")  
    s = "1001010"
    k = 5
    print(f"\nTracing Example 1: s='{s}', k={k}")
    print("Processing from right to left:")
    
    zeros = s.count('0')
    print(f"Total zeros: {zeros}")
    
    value = 0
    ones_count = 0
    bit_position = 0
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            potential_value = value + (1 << bit_position)
            if potential_value <= k:
                value = potential_value
                ones_count += 1
                print(f"Position {i}: '{s[i]}' -> Include (value becomes {value})")
            else:
                print(f"Position {i}: '{s[i]}' -> Skip (would make value {potential_value} > {k})")
        else:
            print(f"Position {i}: '{s[i]}' -> Always include")
        bit_position += 1
    
    print(f"Final: zeros={zeros} + ones={ones_count} = {zeros + ones_count}")
    print(f"\nAdditional tests:")
    print(f"longestSubsequence('111', 3): {sol.longestSubsequence('111', 3)}")  
    print(f"longestSubsequence('000', 0): {sol.longestSubsequence('000', 0)}")  
    print(f"longestSubsequence('1', 0): {sol.longestSubsequence('1', 0)}")      

test_solution()