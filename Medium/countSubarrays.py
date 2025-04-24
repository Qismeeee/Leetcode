class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_distinct = len(set(nums))
        n = len(nums)
        count = 0
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == total_distinct:
                    count += 1
        return count


sol = Solution()
print(sol.countCompleteSubarrays([1, 3, 1, 2, 2]))  
print(sol.countCompleteSubarrays([5, 5, 5, 5]))    
print(sol.countCompleteSubarrays([1]))             
print(sol.countCompleteSubarrays([1, 2, 3]))       
print(sol.countCompleteSubarrays([1, 2, 1, 2, 3]))  
