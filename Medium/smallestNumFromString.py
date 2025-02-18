class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        result = []
        stack = []
        n = len(pattern)
        
        for i in range(n + 1):
            stack.append(i + 1)
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        
        return ''.join(result)


def test_smallestNumber():
    solution = Solution()

    # Test Case 1: Pattern with alternating 'I' and 'D'
    pattern1 = "IIIDIDDD"
    print(f"Test Case 1: {pattern1} -> {solution.smallestNumber(pattern1)}")  

    # Test Case 2: Pattern with all 'D's (decreasing)
    pattern2 = "DDD"
    print(f"Test Case 2: {pattern2} -> {solution.smallestNumber(pattern2)}")  

    # Test Case 3: Pattern with all 'I's (increasing)
    pattern3 = "III"
    print(f"Test Case 3: {pattern3} -> {solution.smallestNumber(pattern3)}") 

    # Test Case 4: Empty pattern (no conditions)
    pattern4 = ""
    print(f"Test Case 4: {pattern4} -> {solution.smallestNumber(pattern4)}")  

    # Test Case 5: Single 'D' pattern
    pattern5 = "D"
    print(f"Test Case 5: {pattern5} -> {solution.smallestNumber(pattern5)}") 

    # Test Case 6: Single 'I' pattern
    pattern6 = "I"
    print(f"Test Case 6: {pattern6} -> {solution.smallestNumber(pattern6)}")  

test_smallestNumber()