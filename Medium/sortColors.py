class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

def test_sortColors():
    solution = Solution()

    # Test case 1
    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    assert nums1 == [0, 0, 1, 1, 2, 2]

    # Test case 2
    nums2 = [2, 0, 1]
    solution.sortColors(nums2)
    assert nums2 == [0, 1, 2]

    # Test case 3
    nums3 = [0]
    solution.sortColors(nums3)
    assert nums3 == [0]

    # Test case 4
    nums4 = [1, 2, 0]
    solution.sortColors(nums4)
    assert nums4 == [0, 1, 2]

    # Test case 5
    nums5 = [2, 2, 2, 1, 1, 0, 0, 0]
    solution.sortColors(nums5)
    assert nums5 == [0, 0, 0, 1, 1, 2, 2, 2]

    print("All test cases passed.")

test_sortColors()
