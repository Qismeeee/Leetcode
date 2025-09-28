class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:
                return a + b + c
        return 0


def run_tests():
    s = Solution()
    cases = [
        ([2,1,2], 5),
        ([1,2,1,10], 0),
        ([3,2,3,4], 10),
        ([3,6,2,3], 8),
        ([1,1,1,1], 3),
        ([10,15,7], 32),
        ([1,1,2], 0),
    ]
    for nums, expected in cases:
        out = s.largestPerimeter(nums)
        assert out == expected, f"{nums}: expected {expected}, got {out}"
        print(nums, out)

run_tests()
