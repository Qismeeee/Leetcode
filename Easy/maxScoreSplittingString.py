class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        total_ones = s.count('1')
        current_zeros = 0
        current_ones = total_ones

        for i in range(len(s) - 1):  # Exclude the last character to ensure non-empty right substring
            if s[i] == '0':
                current_zeros += 1
            else:
                current_ones -= 1
            current_score = current_zeros + current_ones
            max_score = max(max_score, current_score)

        return max_score

# Test cases
def test_maxScore():
    solution = Solution()

    # Test case 1
    s1 = "011101"
    assert solution.maxScore(s1) == 5, f"Test case 1 failed: {solution.maxScore(s1)}"

    # Test case 2
    s2 = "00111"
    assert solution.maxScore(s2) == 5, f"Test case 2 failed: {solution.maxScore(s2)}"

    # Test case 3
    s3 = "1111"
    assert solution.maxScore(s3) == 3, f"Test case 3 failed: {solution.maxScore(s3)}"

    # Test case 4
    s4 = "00000"
    assert solution.maxScore(s4) == 4, f"Test case 4 failed: {solution.maxScore(s4)}"

    # Test case 5
    s5 = "101010"
    assert solution.maxScore(s5) == 3, f"Test case 5 failed: {solution.maxScore(s5)}"

    print("All test cases passed!")

test_maxScore()
