class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sums[0] = current_sum
        
        for i in range(1, len(sums)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum
        
        left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
        right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best
        
        max_sum = 0
        result = []

        for mid in range(k, len(sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]
        
        return result


nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
solution = Solution()
print(solution.maxSumOfThreeSubarrays(nums, k))