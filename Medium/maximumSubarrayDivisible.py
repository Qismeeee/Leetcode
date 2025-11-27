class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        INF = 10**30
        # min_prefix[r] = minimum prefix sum seen so far with index % k == r
        min_prefix = [INF] * k
        min_prefix[0] = 0  # prefix at index 0 has sum 0 and 0 % k == 0

        ans = -INF
        for j in range(1, n + 1):
            r = j % k
            # subarray (i..j-1) has length divisible by k iff i % k == j % k
            if min_prefix[r] != INF:
                ans = max(ans, pref[j] - min_prefix[r])
            # update minimum prefix for this remainder
            if pref[j] < min_prefix[r]:
                min_prefix[r] = pref[j]

        return ans

# Test cases
s = Solution()

print(s.maxSubarraySum([1, 2], 1))            # Expected: 3
print(s.maxSubarraySum([-1,-2,-3,-4,-5], 4))  # Expected: -10
print(s.maxSubarraySum([-5,1,2,-3,4], 2))     # Expected: 4

# Thêm vài test nhỏ
print(s.maxSubarraySum([5], 1))               # Expected: 5
print(s.maxSubarraySum([5], 1))               # Expected: 5
print(s.maxSubarraySum([3, -1, 4, -1, 5], 2)) # Check: length divisible by 2
