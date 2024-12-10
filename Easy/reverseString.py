class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            print(f"Before swap: {s}, left: {s[left]}, right: {s[right]}")
            s[left], s[right] = s[right], s[left]
            print(f"After swap: {s}, left: {s[left]}, right: {s[right]}")
            left += 1
            right -= 1
    
solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s) 
s = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s)
print(s) 
