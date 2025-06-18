class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            triplet = nums[i:i+3]
            if triplet[-1] - triplet[0] > k:
                return []
            res.append(triplet)
        return res