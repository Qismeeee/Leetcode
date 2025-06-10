from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        freq = Counter(s)
        odd = [c for c in freq.values() if c % 2 == 1]
        even = [c for c in freq.values() if c % 2 == 0]
        return max(odd) - min(even)