class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        MOD = 10**9 + 7
        n = len(nums)
        right = Counter(nums)
        left = Counter()

        ans = 0
        for j in range(n):
            mid = nums[j]
            right[mid] -= 1  
            target = mid * 2
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            ans = (ans + left_count * right_count) % MOD
            left[mid] += 1

        return ans % MOD



s = Solution()
# Test 1
nums = [6,3,6]
print("Test 1:", s.specialTriplets(nums))  

# Test 2
nums = [0,1,0,0]
print("Test 2:", s.specialTriplets(nums)) 

# Test 3
nums = [8,4,2,8,4]
print("Test 3:", s.specialTriplets(nums))  

# Test 4: No triplet
nums = [1,2,3,4]
print("Test 4:", s.specialTriplets(nums)) 

# Test 5: All zeros
nums = [0,0,0,0]
print("Test 5:", s.specialTriplets(nums))  
