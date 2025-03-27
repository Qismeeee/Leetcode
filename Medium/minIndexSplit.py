from collections import Counter
class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        n = len(nums)
        count = Counter(nums)
        dominant = max(count, key=count.get)
        majority = n // 2  
        left_count = Counter()
        right_count = count.copy()
        
        for i in range(n - 1):  
            left_count[nums[i]] += 1
            right_count[nums[i]] -= 1
            if right_count[nums[i]] == 0:
                del right_count[nums[i]]  
            if left_count[dominant] * 2 > i + 1 and right_count[dominant] * 2 > n - i - 1:
                return i 
        
        return -1  
    
solution = Solution()
print(solution.minimumIndex([1, 2, 2, 2]))  
print(solution.minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]))  
print(solution.minimumIndex([3, 3, 3, 3, 7, 2, 2]))