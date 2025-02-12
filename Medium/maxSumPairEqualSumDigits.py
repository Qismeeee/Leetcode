class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))
        sum_digit_map = {}
        
        for num in nums:
            digit_sum = sum_of_digits(num)
            if digit_sum in sum_digit_map:
                sum_digit_map[digit_sum].append(num)
            else:
                sum_digit_map[digit_sum] = [num]
        
        max_sum = -1
        for nums_with_same_sum in sum_digit_map.values():
            if len(nums_with_same_sum) > 1:
                nums_with_same_sum.sort(reverse=True)
                max_sum = max(max_sum, nums_with_same_sum[0] + nums_with_same_sum[1])
        
        return max_sum

# Test case 1
nums1 = [18, 43, 36, 13, 7]
sol = Solution()
print(sol.maximumSum(nums1)) 
# Test case 2
nums2 = [10, 12, 19, 14]
print(sol.maximumSum(nums2))  
# Test case 3
nums3 = [123, 321, 111, 222]
print(sol.maximumSum(nums3)) 
# Test case 4
nums4 = [99, 18, 27, 81]
print(sol.maximumSum(nums4)) 
# Test case 5
nums5 = [1, 2, 3, 4, 5]
print(sol.maximumSum(nums5))  
