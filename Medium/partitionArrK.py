class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 1
        start = nums[0]
        for x in nums[1:]:
            if x - start > k:
                count += 1
                start = x
        return count
    
if __name__ == "__main__":
    tests = [
        ([3,6,1,2,5], 2, 2),
        ([1,2,3], 1, 2),
        ([2,2,4,5], 0, 3),
        ([1,5,9,14,15], 4, 2),  
        ([10,1,12,3,8,7], 3, 2),
    ]
    for nums, k, expected in tests:
        result = Solution().partitionArray(nums[:], k)
        print(f"nums={nums}, k={k} -> {result} (expected {expected})", 
              "PASS" if result == expected else "FAIL")