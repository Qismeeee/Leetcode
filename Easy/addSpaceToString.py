class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []  
        space_set = set(spaces)  
        for i, char in enumerate(s):
            if i in space_set:
                result.append(' ')  
        return ''.join(result)  


# Test cases
solution = Solution()

s1 = "LeetcodeHelpsMeLearn"
spaces1 = [8, 13, 15]
result1 = solution.addSpaces(s1, spaces1)
print("Test Case 1 Result:", result1) 

s2 = "icodeinpython"
spaces2 = [1, 5, 7, 9]
result2 = solution.addSpaces(s2, spaces2)
print("Test Case 2 Result:", result2) 

s3 = "spacing"
spaces3 = [0, 1, 2, 3, 4, 5, 6]
result3 = solution.addSpaces(s3, spaces3)
print("Test Case 3 Result:", result3)  
