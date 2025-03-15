class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = min(nums)
        right = max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if self.canRobKHouses(nums, mid, k):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    def canRobKHouses(self, nums, capability, k):
        """
        Determines if it's possible to rob at least k houses with the given capability
        """
        count = 0
        i = 0

        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2  
            else:
                i += 1
            if count >= k:
                return True
                
        return count >= k
    
def test_min_capability():
    solution = Solution()
    
    # Test case 1: Ví dụ từ đề bài
    nums1 = [2, 3, 5, 9]
    k1 = 2
    result1 = solution.minCapability(nums1, k1)
    print(f"Test case 1: {result1}")
    
    # Test case 2: Ví dụ từ đề bài
    nums2 = [2, 7, 9, 3, 1]
    k2 = 2
    result2 = solution.minCapability(nums2, k2)
    print(f"Test case 2: {result2}")
    
    # Test case 3: Trường hợp đơn giản
    nums3 = [1, 2, 3, 4, 5]
    k3 = 3
    result3 = solution.minCapability(nums3, k3)
    print(f"Test case 3: {result3}")
    
    # Test case 4: Trường hợp tất cả giá trị bằng nhau
    nums4 = [5, 5, 5, 5, 5]
    k4 = 2
    result4 = solution.minCapability(nums4, k4)
    print(f"Test case 4: {result4}")
    
    # Test case 5: Trường hợp k = 1
    nums5 = [10, 8, 6, 4, 2]
    k5 = 1
    result5 = solution.minCapability(nums5, k5)
    print(f"Test case 5: {result5}")
    
    # Test case 6: Trường hợp k lớn
    nums6 = [3, 7, 9, 5, 2, 1, 8, 4]
    k6 = 4
    result6 = solution.minCapability(nums6, k6)
    print(f"Test case 6: {result6}")
    
    # Test case 7: Dãy dài hơn
    nums7 = [6, 1, 5, 3, 8, 9, 2, 7, 4, 10]
    k7 = 3
    result7 = solution.minCapability(nums7, k7)
    print(f"Test case 7: {result7}")

if __name__ == "__main__":
    test_min_capability()