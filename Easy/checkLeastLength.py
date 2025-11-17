class Solution(object):
    def kLengthApart(self, nums, k):
        last = -1
        for i, v in enumerate(nums):
            if v == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        return True
