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
