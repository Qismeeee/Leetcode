class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count
    

solution = Solution()
words1 = ["a", "aba", "ababa", "aa"]
print(solution.countPrefixSuffixPairs(words1)) 

words2 = ["pa", "papa", "ma", "mama"]
print(solution.countPrefixSuffixPairs(words2))  

words3 = ["abab", "ab"]
print(solution.countPrefixSuffixPairs(words3)) 
