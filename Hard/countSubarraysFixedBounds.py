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
    

def test_count_subarrays():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3, 5, 2, 7, 5]
    minK1 = 1
    maxK1 = 5
    assert solution.countSubarrays(nums1, minK1, maxK1) == 2
    
    # Test case 2
    nums2 = [1, 1, 1, 1]
    minK2 = 1
    maxK2 = 1
    assert solution.countSubarrays(nums2, minK2, maxK2) == 10
    
    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    minK3 = 2
    maxK3 = 4
    assert solution.countSubarrays(nums3, minK3, maxK3) == 3
    
    # Test case 4
    nums4 = [5, 1, 3, 5, 8, 2]
    minK4 = 1
    maxK4 = 5
    assert solution.countSubarrays(nums4, minK4, maxK4) == 4
    
    # Test case 5
    nums5 = [3, 3, 3, 3, 3]
    minK5 = 3
    maxK5 = 3
    assert solution.countSubarrays(nums5, minK5, maxK5) == 15
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_count_subarrays()