class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        best = 0
        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left)
        return best


def run_tests():
    sol = Solution()
    cases = [
        ([1,1,0,1], 3),
        ([0,1,1,1,0,1,1,0,1], 5),
        ([1,1,1], 2),
        ([0,0,0], 0),
        ([1,0,1,1,0,1], 3),
        ([1,0,0,1], 1),
        ([1,0,1,1,1], 4),
        ([0,1,1,1,1,1,1,1,1,0], 8),
        ([1], 0),
        ([0,1,0,1,1,1,0], 4),
    ]
    for nums, expected in cases:
        got = sol.longestSubarray(nums)
        assert got == expected, (nums, expected, got)
    print("OK")

run_tests()
