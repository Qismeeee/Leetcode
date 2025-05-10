class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        if z1 == 0 and z2 == 0:
            return sum1 if sum1 == sum2 else -1
        if z1 == 0:
            S = sum1
            return S if S - sum2 >= z2 else -1
        if z2 == 0:
            S = sum2
            return S if S - sum1 >= z1 else -1
        S = max(sum1 + z1, sum2 + z2)
        return S


print(Solution().minSum([3,2,0,1,0], [6,5,0]))
print(Solution().minSum([2,0,2,0], [1,4]))