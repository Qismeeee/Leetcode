class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"        
        for _ in range(1, n):
            next_result = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                next_result += str(count) + result[i]
                i += 1
            result = next_result
        return result

solution = Solution()

test_cases = [1, 2, 3, 4, 5]
expected_results = ["1", "11", "21", "1211", "111221"]

for i, test_case in enumerate(test_cases):
    result = solution.countAndSay(test_case)
    assert result == expected_results[i], f"Test case {test_case} failed: expected {expected_results[i]}, got {result}"

print("All test cases passed!")
