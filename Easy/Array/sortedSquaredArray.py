# Using 2 pointers
class Solution:
    def SortedArray(self, arr):
        res = [0] * len(arr)
        left, right = 0, len(arr) - 1
        pos = len(arr) - 1
        while left <= right:
            if abs(arr[left]) > abs(arr[right]):
                res[pos] = arr[left] ** 2
                left += 1
            else:
                res[pos] = arr[right] ** 2
                right -= 1
            pos -= 1
        return res

solution = Solution()
sorted = solution.SortedArray([-4, -2, 0, 2, 3])
print(sorted)