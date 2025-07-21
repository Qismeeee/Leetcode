class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            return s
        
        result = []
        
        for char in s:
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        
        return ''.join(result)


# Alternative solution using sliding window approach
class Solution2(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            return s
        
        result = [s[0], s[1]]  
        for i in range(2, len(s)):
            if not (s[i] == result[-1] == result[-2]):
                result.append(s[i])
        
        return ''.join(result)


def test_solution():
    sol = Solution()
    sol2 = Solution2()
    
    test_cases = [
        "leeetcode",
        "aaabaaaa", 
        "aab",
        "a",
        "aa",
        "aaa",
        "aaaa",
        "abcdef"
    ]
    
    for test in test_cases:
        result1 = sol.makeFancyString(test)
        result2 = sol2.makeFancyString(test)
        print("Input: '{}' -> Output: '{}' (both solutions: {})".format(
            test, result1, result1 == result2))

test_solution()