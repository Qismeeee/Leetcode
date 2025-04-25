from collections import defaultdict

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1
        result = 0
        prefix = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1
            mod_val = prefix % modulo
            target = (mod_val - k) % modulo
            result += count[target]
            count[mod_val] += 1

        return result
