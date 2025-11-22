class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        for x in nums:
            if x % 3 != 0:
                ops += 1
        return ops


s = Solution()

print(s.minimumOperations([1,2,3,4]))   # 3
print(s.minimumOperations([3,6,9]))     # 0
print(s.minimumOperations([2,2,2]))     # 3
print(s.minimumOperations([1]))         # 1
print(s.minimumOperations([1,4,7,10]))  # 4
