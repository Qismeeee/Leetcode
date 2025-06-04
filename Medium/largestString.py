class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        n = len(word)
        if numFriends == 1:
            return word  
        ans = ""
        for i in range(n):
            max_len = min(n - i, n - numFriends + 1)  
            t = word[i : i + max_len]                
            if t > ans:
                ans = t                               
        return ans                                   

print(Solution().answerString("dbca", 2))  
print(Solution().answerString("gggg", 4)) 