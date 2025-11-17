class Solution(object):
    def kLengthApart(self, nums, k):
        last = -1
        for i, v in enumerate(nums):
            if v == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        return True

s = Solution()
print(s.kLengthApart([1,0,0,0,1,0,0,1], 2))  # True
print(s.kLengthApart([1,0,0,1,0,1], 2))      # False
print(s.kLengthApart([1,0,1], 1))            # True
print(s.kLengthApart([1,1], 0))              # True
print(s.kLengthApart([1,1], 1))              # False
