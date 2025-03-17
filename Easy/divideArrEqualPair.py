from collections import Counter

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        for value in count.values():
            if value % 2 != 0:
                return False
        
        return True


nums1 = [3, 2, 3, 2, 2, 2]
solution = Solution()
print(solution.divideArray(nums1))  

nums2 = [1, 2, 3, 4]
print(solution.divideArray(nums2)) 

nums3 = [1, 1]
print(solution.divideArray(nums3)) 

nums4 = [1, 2, 2]
print(solution.divideArray(nums4)) 

nums5 = [10, 10, 20, 20, 30, 30]
print(solution.divideArray(nums5)) 