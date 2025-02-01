class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            if (nums[i] % 2) == (nums[i + 1] % 2):  
                return False
        return True


solution = Solution()
# Test case 1: Mảng chỉ có một phần tử
nums1 = [1]
print(solution.isArraySpecial(nums1))  

# Test case 2: Mảng có 3 phần tử với các cặp số có độ chênh lệch parity khác nhau
nums2 = [2, 1, 4]
print(solution.isArraySpecial(nums2)) 

# Test case 3: Mảng có 4 phần tử, một cặp có cùng parity
nums3 = [4, 3, 1, 6]
print(solution.isArraySpecial(nums3)) 

# Test case 4: Mảng có 2 phần tử, với parity khác nhau
nums4 = [5, 8]
print(solution.isArraySpecial(nums4))  

# Test case 5: Mảng có 2 phần tử với parity giống nhau
nums5 = [6, 8]
print(solution.isArraySpecial(nums5))  
