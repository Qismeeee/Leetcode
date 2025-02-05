class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        diff = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        if len(diff) != 2:
            return False
        i, j = diff
        return s1[i] == s2[j] and s1[j] == s2[i]


# Test case 1: Hai chuỗi đã bằng nhau
s1 = "kelb"
s2 = "kelb"
solution = Solution()
print(solution.areAlmostEqual(s1, s2)) 

# Test case 2: Hai chuỗi có thể trở thành giống nhau bằng một phép hoán đổi
s1 = "bank"
s2 = "kanb"
print(solution.areAlmostEqual(s1, s2))  

# Test case 3: Hai chuỗi không thể trở thành giống nhau dù có hoán đổi
s1 = "attack"
s2 = "defend"
print(solution.areAlmostEqual(s1, s2))  

# Test case 4: Hai chuỗi khác nhau nhưng có thể hoán đổi một lần
s1 = "abcd"
s2 = "abdc"
print(solution.areAlmostEqual(s1, s2))  

# Test case 5: Một chuỗi có chỉ một ký tự khác, không thể làm chúng bằng nhau
s1 = "abc"
s2 = "abz"
print(solution.areAlmostEqual(s1, s2))  
