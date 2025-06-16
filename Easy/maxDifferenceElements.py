class Solution(object):
    def maximumDifference(self, nums):
        min_val = nums[0]
        max_diff = -1
        for x in nums[1:]:
            if x > min_val:
                max_diff = max(max_diff, x - min_val)
            else:
                min_val = x
        return max_diff
    
if __name__ == "__main__":
    tests = [
        ([7, 1, 5, 4], 4),
        ([9, 4, 3, 2], -1),
        ([1, 5, 2, 10], 9),
        ([2, 3], 1),
        ([5, 5, 5], -1),
    ]
    for nums, expected in tests:
        result = Solution().maximumDifference(nums)
        status = 'PASS' if result == expected else 'FAIL'
        print(f"nums={nums} -> {result} (expected {expected}) {status}")