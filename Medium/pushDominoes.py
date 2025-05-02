class Solution(object):
    def pushDominoes(self, dominoes):
        s = 'L' + dominoes + 'R'
        res = list(s)
        i = 0
        for j in range(1, len(s)):
            if s[j] == '.':
                continue
            if j - i > 1:
                if s[i] == s[j]:
                    for k in range(i + 1, j):
                        res[k] = s[i]
                elif s[i] == 'R' and s[j] == 'L':
                    l, r = i + 1, j - 1
                    while l < r:
                        res[l] = 'R'
                        res[r] = 'L'
                        l += 1
                        r -= 1
            i = j
        return ''.join(res[1:-1])


if __name__ == "__main__":
    s = Solution()
    print(s.pushDominoes("RR.L"))
    print(s.pushDominoes(".L.R...LR..L.."))