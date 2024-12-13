# Mảng đơn điệu
class Solution:
    def monotonicArray(self, arr):
        is_increasing = True
        is_decreasing = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                is_increasing = False
            if arr[i] < arr[i + 1]:
                is_decreasing = False
        return is_increasing or is_decreasing

s = Solution()
print(s.monotonicArray([1,2,3,4]))
print(s.monotonicArray([1,2,2,4]))
print(s.monotonicArray([5,6,8,7]))
print(s.monotonicArray([9,8,7,7]))


