import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        operations = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_elem = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_elem)
            operations += 1
        
        return operations

# Test case 1
nums1 = [2, 11, 10, 1, 3]
k1 = 10
solution1 = Solution()
print(f"Test case 1: {solution1.minOperations(nums1, k1)}")  

# Test case 2
nums2 = [1, 1, 2, 4, 9]
k2 = 20
solution2 = Solution()
print(f"Test case 2: {solution2.minOperations(nums2, k2)}") 

# Test case 3 (already all elements >= k)
nums3 = [10, 20, 30]
k3 = 10
solution3 = Solution()
print(f"Test case 3: {solution3.minOperations(nums3, k3)}") 

# Test case 4 (edge case with smallest length)
nums4 = [1, 5]
k4 = 10
solution4 = Solution()
print(f"Test case 4: {solution4.minOperations(nums4, k4)}")  
