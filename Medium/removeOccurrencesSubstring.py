class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while part in s:
            index = s.find(part)
            s = s[:index] + s[index + len(part):]
        return s
    
def test_removeOccurrences():
    solution = Solution()
    
    assert solution.removeOccurrences("daabcbaabcbc", "abc") == "dab"
    assert solution.removeOccurrences("axxxxyyyyb", "xy") == "ab"
    assert solution.removeOccurrences("hello", "xyz") == "hello"
    assert solution.removeOccurrences("aaaa", "a") == ""
    assert solution.removeOccurrences("abc", "abc") == ""
    print("All test cases passed!")

test_removeOccurrences()