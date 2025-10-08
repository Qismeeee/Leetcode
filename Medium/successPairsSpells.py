import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        m = len(potions)
        potions.sort()
        res = []
        for s in spells:
            need = (success + s - 1) // s
            idx = bisect.bisect_left(potions, need)
            res.append(m - idx)
        return res
