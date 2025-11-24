class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        cur = 0
        for b in nums:
            cur = ((cur << 1) + b) % 5
            res.append(cur == 0)
        return res

s = Solution()

print(s.prefixesDivBy5([0,1,1]))   # [True, False, False]
print(s.prefixesDivBy5([1,1,1]))   # [False, False, False]
print(s.prefixesDivBy5([1,0,1,0])) # [False, False, False, False]
print(s.prefixesDivBy5([1,0,0,1,0])) # e.g., [False, False, False, False, True]
