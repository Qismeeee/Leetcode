
class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        groups = []
        i = 0
        
        while i < len(word):
            char = word[i]
            count = 1
            while i + count < len(word) and word[i + count] == char:
                count += 1
            
            groups.append(count)
            i += count
        total = 1  
        for group_length in groups:
            if group_length > 1:
                total += group_length - 1
        
        return total