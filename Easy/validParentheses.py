class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}':'{', ']':'['}
        for char in s:
            if char in mapping:
                print(char)
                print(mapping[char])
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
solution = Solution()
s = "()"
print(solution.isValid(s))