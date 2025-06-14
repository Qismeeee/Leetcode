class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        stacks = [[] for _ in range(26)]
        removed = [False] * n

        for i, ch in enumerate(s):
            if ch != '*':
                ci = ord(ch) - ord('a')
                stacks[ci].append(i)
            else:
                for ci in range(26):
                    if stacks[ci]:
                        idx = stacks[ci].pop()  
                        removed[idx] = True
                        break
        res = []
        for i, ch in enumerate(s):
            if ch != '*' and not removed[i]:
                res.append(ch)
        return ''.join(res)


tests = [
    ("aaba*", "aab"),
    ("abc",   "abc"),
    ("a*b*c*", ""),
]

for s, expected in tests:
    result = Solution().clearStars(s)
    assert result == expected, f"{s}: expected {expected}, got {result}"

print("All simple tests passed")
