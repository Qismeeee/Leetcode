class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans

def run_tests():
    s = Solution()
    cases = [
        ([2,2,3,4], 3),
        ([4,2,3,4], 4),
        ([0,0,0], 0),
        ([1,1,1], 1),
        ([2,3,4,5,6], 7),
        ([1,2,2,3,4], 7),
        ([2], 0),
        ([], 0),
    ]
    for nums, expected in cases:
        out = s.triangleNumber(nums)
        assert out == expected, f"{nums}: expected {expected}, got {out}"
        print(nums, out)

run_tests()
