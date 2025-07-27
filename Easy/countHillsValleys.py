class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        i = 1  
        while i < n - 1:  
            left_neighbor = None
            for j in range(i - 1, -1, -1):
                if nums[j] != nums[i]:
                    left_neighbor = nums[j]
                    break
            right_neighbor = None
            for j in range(i + 1, n):
                if nums[j] != nums[i]:
                    right_neighbor = nums[j]
                    break
            
            if left_neighbor is not None and right_neighbor is not None:
                current = nums[i]
                if current > left_neighbor and current > right_neighbor:
                    count += 1
                    while i + 1 < n and nums[i + 1] == current:
                        i += 1
                
                elif current < left_neighbor and current < right_neighbor:
                    count += 1
                    while i + 1 < n and nums[i + 1] == current:
                        i += 1
            
            i += 1
        
        return count