class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)

        cnt1 = nums.count(1)
        if cnt1 > 0:
            return n - cnt1

        best = float('inf')
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        if best == float('inf'):
            return -1

        return best + n - 2
