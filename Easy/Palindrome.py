class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return x == reverse or x == reverse // 10
    
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
    

# Test cases
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(123))
print(s.isPalindrome2("abc"))  
print(s.isPalindrome2("abc")) 

