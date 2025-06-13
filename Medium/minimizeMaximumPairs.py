class Solution(object):
    def minimizeMax(self, nums, p):
        if p == 0 or len(nums) < 2:
            return 0

        nums.sort()

        def can_make(d):
            pairs = 0
            i = 0
            n = len(nums)
            while i < n - 1:
                if nums[i + 1] - nums[i] <= d:
                    pairs += 1
                    i += 2          
                else:
                    i += 1
                if pairs >= p:     
                    return True
            return False

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
