class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        result = 0
        last_out_of_bounds = -1
        last_min = -1
        last_max = -1
        
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                last_out_of_bounds = i
            
            if nums[i] == minK:
                last_min = i
            if nums[i] == maxK:
                last_max = i
            
            if last_min > last_out_of_bounds and last_max > last_out_of_bounds:
                result += min(last_min, last_max) - last_out_of_bounds
        
        return result