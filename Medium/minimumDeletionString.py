class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        freq = Counter(word)
        frequencies = sorted(freq.values())
        if not frequencies:
            return 0
        
        min_deletions = len(word) 
        for min_f in range(1, max(frequencies) + 1):
            deletions = 0
            
            for orig_f in frequencies:
                if orig_f < min_f:
                    deletions += orig_f
                else:
                    keep = min(orig_f, min_f + k)
                    deletions += orig_f - keep
            
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions