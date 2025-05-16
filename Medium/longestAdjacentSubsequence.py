class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        dp = [(1, -1) for _ in range(n)]
        best_end = 0

        def hamming1(a, b):
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] and len(words[j]) == len(words[i]) and hamming1(words[j], words[i]):
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = (dp[j][0] + 1, j)
            if dp[i][0] > dp[best_end][0]:
                best_end = i

        seq = []
        cur = best_end
        while cur != -1:
            seq.append(words[cur])
            cur = dp[cur][1]
        return seq[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.getWordsInLongestSubsequence(["bab","dab","cab"], [1,2,2]))
    print(sol.getWordsInLongestSubsequence(["a","b","c","d"], [1,2,3,4]))
