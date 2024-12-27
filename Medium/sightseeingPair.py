class Solution(object):
    def maxScoreSightseeingPair(self, values):

        max_score = 0
        max_value_plus_i = values[0] + 0 
        for j in range(1, len(values)):
            current_score = max_value_plus_i + values[j] - j
            max_score = max(max_score, current_score)
            max_value_plus_i = max(max_value_plus_i, values[j] + j)
        return max_score
    

def test_maxScoreSightseeingPair():
    solution = Solution()
    
    # Test case 1: Example từ đề bài
    assert solution.maxScoreSightseeingPair([8,1,5,2,6]) == 11
    print("Test case 1 passed!")
    
    # Test case 2: Example từ đề bài
    assert solution.maxScoreSightseeingPair([1,2]) == 2
    print("Test case 2 passed!")
    
    # Test case 3: Array với các giá trị giống nhau
    assert solution.maxScoreSightseeingPair([5,5,5,5,5]) == 9
    print("Test case 3 passed!")
    
    # Test case 4: Array với giá trị giảm dần
    assert solution.maxScoreSightseeingPair([10,9,8,7,6]) == 18
    print("Test case 4 passed!")
    
    # Test case 5: Array với giá trị tăng dần
    assert solution.maxScoreSightseeingPair([1,2,3,4,5]) == 8
    print("Test case 5 passed!")
    
    # Test case 6: Array lớn hơn với các giá trị ngẫu nhiên
    assert solution.maxScoreSightseeingPair([1,3,5,7,9,11,13,15]) == 27  # Sửa từ 21 thành 27
    print("Test case 6 passed!")
    
    # Test case 7: Array với giá trị tối thiểu
    assert solution.maxScoreSightseeingPair([1,1,1,1]) == 1
    print("Test case 7 passed!")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_maxScoreSightseeingPair()