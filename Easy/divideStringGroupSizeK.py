class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        result = []
        
        for i in range(0, len(s), k):
            group = s[i:i+k]
            if len(group) < k:
                group += fill * (k - len(group))
            
            result.append(group)
        
        return result

def test_solution():
    sol = Solution()
    result1 = sol.divideString("abcdefghi", 3, "x")
    print(f"Example 1: {result1}")  
    result2 = sol.divideString("abcdefghij", 3, "x")
    print(f"Example 2: {result2}")  
    result3 = sol.divideString("a", 5, "z")
    print(f"Test 3: {result3}")  
    
    result4 = sol.divideString("abcd", 2, "y")
    print(f"Test 4: {result4}")  

test_solution()