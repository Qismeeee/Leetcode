from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        cnt = Counter(nums)
        m = max(cnt.values())
        return sum(f for f in cnt.values() if f == m)


def run_tests():
    s = Solution()
    cases = [
        ([1,2,2,3,1,4], 4),
        ([1,2,3,4,5], 5),
        ([7,7,7,7], 4),
        ([1], 1),
        ([1,1,2,2,3,3], 6),
        ([10,20,20,30,30,30], 3),
    ]
    for nums, expected in cases:
        out = s.maxFrequencyElements(nums)
        assert out == expected, f"{nums}: expected {expected}, got {out}"
        print(nums, out)

run_tests()
