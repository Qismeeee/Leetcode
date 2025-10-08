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


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
s = Solution()
print(s.successfulPairs(spells, potions, success))
