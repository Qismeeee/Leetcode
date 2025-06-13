from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0 or len(nums) < 2:
            return 0
        nums.sort()
        def ok(d):
            cnt, i, n = 0, 0, len(nums)
            while i < n - 1:
                if nums[i + 1] - nums[i] <= d:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt >= p:
                    return True
            return False
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            hi = mid if ok(mid) else mid + 1 if (lo := mid + 1) else hi
        return lo

tests = [
    ([10, 1, 2, 7, 1, 3], 2, 1),
    ([4, 2, 1, 2],          1, 0),
    ([5, 5, 5, 5],          2, 0),
    ([1, 6, 9, 15, 19],     2, 4),
    ([1],                   0, 0)         
]

sol = Solution()
for nums, p, expect in tests:
    out = sol.minimizeMax(nums[:], p)
    print(f"nums={nums}, p={p} -> {out}  (expected {expect})",
          "✅" if out == expect else "❌")
