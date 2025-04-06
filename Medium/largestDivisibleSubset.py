class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        dp = [1] * n  
        prev = [-1] * n  
        max_size = 1
        max_index = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        return result[::-1]
