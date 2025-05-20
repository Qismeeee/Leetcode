class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        cover = [0] * (n + 1)
        for l, r in queries:
            cover[l] += 1
            if r + 1 < n:
                cover[r + 1] -= 1
        for i in range(n):
            if i > 0:
                cover[i] += cover[i - 1]
            if cover[i] < nums[i]:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isZeroArray([1, 0, 1], [[0, 2]]))
    print(sol.isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]))
    print(sol.isZeroArray([2, 2, 2], [[0, 1], [1, 2]]))
    print(sol.isZeroArray([0, 0, 0], [[0, 2]]))