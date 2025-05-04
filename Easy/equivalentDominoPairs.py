from collections import Counter

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        cnt = Counter()
        res = 0
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            res += cnt[key]
            cnt[key] += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
    print(s.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))