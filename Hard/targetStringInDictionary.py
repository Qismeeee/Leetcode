class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)

        char_count = [[0] * 26 for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][ord(char) - ord('a')] += 1
        dp = [0] * (n + 1)
        dp[0] = 1  

        for i in range(m):
            for j in range(n - 1, -1, -1):
                char_idx = ord(target[j]) - ord('a')
                dp[j + 1] += dp[j] * char_count[i][char_idx]
                dp[j + 1] %= MOD

        return dp[n]
    

solution = Solution()
words = ["acca", "bbbb", "caca"]
target = "aba"
print(solution.numWays(words, target))  

words = ["abba", "baab"]
target = "bab"
print(solution.numWays(words, target))  