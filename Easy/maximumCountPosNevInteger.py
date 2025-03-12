class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_first_positive_index(nums):
            low = 0
            high = len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > 0:
                    high = mid
                else:
                    low = mid + 1
            return low

        def find_last_negative_index(nums):
            low = -1
            high = len(nums) - 1
            while low < high:
                mid = (low + high + 1) // 2
                if nums[mid] < 0:
                    low = mid
                else:
                    high = mid - 1
            return low

        first_pos_index = find_first_positive_index(nums)
        last_neg_index = find_last_negative_index(nums)

        pos_count = len(nums) - first_pos_index
        neg_count = 0 if last_neg_index == -1 else last_neg_index + 1

        return max(pos_count, neg_count)
    

nums1 = [-3, -2, -1, 0, 0, 1, 2]
print(Solution().maximumCount(nums1))

nums2 = [-5, -4, -3, 1, 2, 3]
print(Solution().maximumCount(nums2))

nums3 = [1, 2, 3, 4, 5]
print(Solution().maximumCount(nums3))

nums4 = [-1, -2, -3, -4]
print(Solution().maximumCount(nums4))

nums5 = [0, 0, 0, 0]
print(Solution().maximumCount(nums5))

nums6 = [1]
print(Solution().maximumCount(nums6))

nums7 = [-1]
print(Solution().maximumCount(nums7))