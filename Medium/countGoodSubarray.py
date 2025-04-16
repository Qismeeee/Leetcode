class Solution:
    def countGood(self, nums, k):
        from collections import defaultdict
        l = r = count = ans = 0
        mp = defaultdict(int)
        n = len(nums)
        while r < n:
            count += mp[nums[r]]
            mp[nums[r]] += 1
            while l < n and (count - (mp[nums[l]] - 1)) >= k:
                mp[nums[l]] -= 1
                count -= mp[nums[l]]
                l += 1
            if count >= k:
                ans += (l + 1)
            r += 1
        return ans
    

def test_solution():
    test_cases = [
        ([1, 1, 1, 1, 1], 10, 1),
        ([3, 1, 4, 3, 2, 2, 4], 2, 4),
        ([1, 2, 3, 4, 5], 2, 0),
        ([5, 5, 5, 5, 5], 5, 10),
        ([1, 2, 1, 2, 1, 2], 4, 4),
    ]

    for idx, (nums, k, expected) in enumerate(test_cases):
        result = Solution().countGood(nums, k)
        assert result == expected, f"Test case {idx + 1} failed: expected {expected}, got {result}"

    print("All test cases passed!")

test_solution()