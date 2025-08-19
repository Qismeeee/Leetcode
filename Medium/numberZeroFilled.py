class Solution(object):
    def zeroFilledSubarray(self, nums):
        res = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
                res += run
            else:
                run = 0
        return res


def run_tests():
    sol = Solution()
    cases = [
        ([1,3,0,0,2,0,0,4], 6),
        ([0,0,0,2,0,0], 9),
        ([2,10,2019], 0),
        ([0], 1),
        ([0,0,0,0], 10),
        ([1,0,0,0,1], 6),
        ([0,1,0,0], 4),
        ([1,1,1], 0),
    ]
    for nums, expected in cases:
        got = sol.zeroFilledSubarray(nums)
        assert got == expected, (nums, expected, got)
    print("OK")

run_tests()
