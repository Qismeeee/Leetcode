class Solution(object):
    def countPalindromicSubsequence(self, s):
        first = [-1] * 26
        last = [-1] * 26
        n = len(s)

        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
        for c in range(26):
            if first[c] != -1 and last[c] > first[c]:
                seen = set()
                for i in range(first[c] + 1, last[c]):
                    seen.add(s[i])
                ans += len(seen)
        return ans


s = Solution()

print(s.countPalindromicSubsequence("aabca"))    # 3
print(s.countPalindromicSubsequence("adc"))      # 0
print(s.countPalindromicSubsequence("bbcbaba"))  # 4
print(s.countPalindromicSubsequence("aaa"))      # 1   ("aaa")
print(s.countPalindromicSubsequence("abba"))     # 2   ("aaa"? no) → ("aba","bbb"? no) → actually only "aba","aaa"? only "aba" = 1
