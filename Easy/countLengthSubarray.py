class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]
            if first + third == middle / 2.0:
                count += 1
        return count

s = Solution()

print(s.countSubarrays([1,2,1,4,1]))  
print(s.countSubarrays([1,1,1]))      
print(s.countSubarrays([2,4,2,8,2])) 
print(s.countSubarrays([0,0,0]))    
print(s.countSubarrays([5,10,5,20,5])) 
