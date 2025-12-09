class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        MOD = 10**9 + 7
        n = len(nums)
        right = Counter(nums)
        left = Counter()

        ans = 0
        for j in range(n):
            mid = nums[j]
            right[mid] -= 1  
            target = mid * 2
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            ans = (ans + left_count * right_count) % MOD
            left[mid] += 1

        return ans % MOD
