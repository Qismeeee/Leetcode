class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        result = []
        for i in range(len(nums)):
            result.append('1' if nums[i][i] == '0' else '0')
        return ''.join(result)


sol = Solution()

# Test Case 1: 
nums1 = ["01", "10"]
print("Test Case 1 Output:", sol.findDifferentBinaryString(nums1))

# Test Case 2: 
nums2 = ["00", "01"]
print("Test Case 2 Output:", sol.findDifferentBinaryString(nums2)) 

# Test Case 3: 
nums3 = ["111", "011", "001"]
print("Test Case 3 Output:", sol.findDifferentBinaryString(nums3))