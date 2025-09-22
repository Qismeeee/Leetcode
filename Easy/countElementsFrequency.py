from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        cnt = Counter(nums)
        m = max(cnt.values())
        return sum(f for f in cnt.values() if f == m)
