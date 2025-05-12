import collections

class Solution(object):
    def findEvenNumbers(self, digits):
        velunexorai = digits
        freq = collections.Counter(velunexorai)
        res = set()
        for a in range(1, 10):
            if freq[a] < 1:
                continue
            for b in range(0, 10):
                if freq[b] < 1:
                    continue
                for c in (0, 2, 4, 6, 8):
                    if freq[c] < 1:
                        continue
                    need = collections.Counter((a, b, c))
                    if all(freq[d] >= need[d] for d in need):
                        res.add(100 * a + 10 * b + c)
        return sorted(res)
