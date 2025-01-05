class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift_array = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift_array[start] += 1
                shift_array[end + 1] -= 1
            else:
                shift_array[start] -= 1
                shift_array[end + 1] += 1
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]

        result = []
        for i in range(n):
            original_char = s[i]
            shift_value = shift_array[i] % 26 
            new_char = chr((ord(original_char) - ord('a') + shift_value) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)

def run_tests():
    solution = Solution()
    s1 = "abc"
    shifts1 = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    print("Test case 1 output:", solution.shiftingLetters(s1, shifts1))  # Expected: "ace"

    s2 = "dztz"
    shifts2 = [[0, 0, 0], [1, 1, 1]]
    print("Test case 2 output:", solution.shiftingLetters(s2, shifts2))  # Expected: "catz"

    s3 = "abcdefghijklmnopqrstuvwxyz"
    shifts3 = [[0, 25, 1], [0, 0, 0], [10, 15, 1]]
    print("Test case 3 output:", solution.shiftingLetters(s3, shifts3))  # Expected: "bcdefghijklmnopqrstuvwxyza"

    s4 = "zzz"
    shifts4 = [[0, 2, 0], [1, 1, 1]]
    print("Test case 4 output:", solution.shiftingLetters(s4, shifts4))  # Expected: "yzy"

    s5 = "a"
    shifts5 = [[0, 0, 1], [0, 0, 0]]
    print("Test case 5 output:", solution.shiftingLetters(s5, shifts5))  # Expected: "b"

run_tests()