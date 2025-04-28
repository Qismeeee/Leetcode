class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        r = 0
        cur_sum = 0
        res = 0
        for l in range(n):
            if r < l:
                r = l
                cur_sum = 0
            while r < n and (cur_sum + nums[r]) * (r - l + 1) < k:
                cur_sum += nums[r]
                r += 1
            res += r - l
            if r > l:
                cur_sum -= nums[l]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countSubarrays([2, 1, 4, 3, 5], 10))  
    print(s.countSubarrays([1, 1, 1], 5))  