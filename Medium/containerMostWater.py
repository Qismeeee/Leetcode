class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate width and height
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            max_area = max(max_area, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

def test_maxArea():
    solution = Solution()
    
    # Test case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    assert solution.maxArea(height1) == 49
    print("Test case 1 passed.")

    # Test case 2
    height2 = [1,1]
    assert solution.maxArea(height2) == 1
    print("Test case 2 passed.")

    # Test case 3
    height3 = [4,3,2,1,4]
    assert solution.maxArea(height3) == 16
    print("Test case 3 passed.")

    # Test case 4
    height4 = [1,2,1]
    assert solution.maxArea(height4) == 2
    print("Test case 4 passed.")

    # Test case 5 - edge case: only two elements
    height5 = [0, 10]
    assert solution.maxArea(height5) == 0
    print("Test case 5 passed.")

test_maxArea()
