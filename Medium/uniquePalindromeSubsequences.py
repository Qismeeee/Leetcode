class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_palindromes = set()
        n = len(s)
        left_chars = [set() for _ in range(n)]
        right_chars = [set() for _ in range(n)]

        for i in range(1, n):
            left_chars[i] = left_chars[i - 1].copy()
            left_chars[i].add(s[i - 1])

        for i in range(n - 2, -1, -1):
            right_chars[i] = right_chars[i + 1].copy()
            right_chars[i].add(s[i + 1])

        for i in range(1, n - 1):
            for char in left_chars[i]:
                if char in right_chars[i]:
                    unique_palindromes.add(char + s[i] + char)

        return len(unique_palindromes)
    

solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))  
print(solution.countPalindromicSubsequence("adc"))   
print(solution.countPalindromicSubsequence("bbcbaba")) 