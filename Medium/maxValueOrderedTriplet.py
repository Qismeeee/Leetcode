class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = 0
        result = 0
        max_i = nums[0]

        for j in range(1, len(nums) - 1):
            max_diff = max(max_diff, max_i - nums[j])
            result = max(result, max_diff * nums[j + 1])
            max_i = max(max_i, nums[j])

        return result

def test():
    sol = Solution()
    
    # Test case 1
    nums1 = [12, 6, 1, 2, 7]
    print("Test case 1:", sol.maximumTripletValue(nums1))  

    # Test case 2
    nums2 = [1, 10, 3, 4, 19]
    print("Test case 2:", sol.maximumTripletValue(nums2))  

    # Test case 3
    nums3 = [1, 2, 3]
    print("Test case 3:", sol.maximumTripletValue(nums3))

test()
