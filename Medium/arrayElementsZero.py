class Solution(object):
    def countValidSelections(self, nums):
        n = len(nums)

        def simulate(start, direction):
            arr = nums[:]  # copy
            curr = start
            d = direction  # -1 for left, +1 for right
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += d
                else:
                    arr[curr] -= 1
                    d = -d
                    curr += d
            for v in arr:
                if v != 0:
                    return False
            return True

        ans = 0
        for i, v in enumerate(nums):
            if v == 0:
                if simulate(i, -1):
                    ans += 1
                if simulate(i, +1):
                    ans += 1
        return ans

nums = [1,0,2,0,3]
s = Solution()
print(s.countValidSelections(nums))  # 2

nums = [2,3,4,0,4,1,0]
print(s.countValidSelections(nums))  # 0

nums = [0]
print(s.countValidSelections(nums))  # 2 (start at 0, left or right)
