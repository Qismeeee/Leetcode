class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drop_count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] < nums[(i - 1) % n]:  
                drop_count += 1
            if drop_count > 1:
                return False
        
        return drop_count <= 1

solution = Solution()
# Test case 1: Array đã được xoay và sắp xếp theo thứ tự không giảm
nums1 = [3, 4, 5, 1, 2]
print(solution.check(nums1))  

# Test case 2: Array không thể là phiên bản xoay của một mảng đã được sắp xếp
nums2 = [2, 1, 3, 4]
print(solution.check(nums2))  

# Test case 3: Array đã được sắp xếp và không xoay
nums3 = [1, 2, 3]
print(solution.check(nums3)) 
# Test case 4: Mảng chỉ có một phần tử (trường hợp biên)
nums4 = [5]
print(solution.check(nums4))  

# Test case 5: Mảng đã sắp xếp nhưng có phần tử trùng lặp
nums5 = [1, 1, 2, 2, 3, 3]
print(solution.check(nums5))  

# Test case 6: Mảng với một lần giảm duy nhất
nums6 = [3, 4, 5, 6, 1, 2]
print(solution.check(nums6)) 

# Test case 7: Mảng không sắp xếp và có nhiều lần giảm
nums7 = [1, 2, 3, 5, 4, 6]
print(solution.check(nums7)) 
