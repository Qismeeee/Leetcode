from collections import Counter

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        deletions = 0
        for c in freq:
            if freq[c] >= 3:
                operations = (freq[c] - 1) // 2
                deletions += 2 * operations
        
        return len(s) - deletions
