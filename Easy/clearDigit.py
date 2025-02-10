class Solution(object):
    def clearDigits(self, s):
        """
      :type s: str
      :rtype: str
        """
        result = []
        for char in s:
            if char.isdigit():
                if result:  
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)
    
s1 = "abc"
s2 = "cb34"

solution = Solution()
print(solution.clearDigits(s1)) 
print(solution.clearDigits(s2)) 