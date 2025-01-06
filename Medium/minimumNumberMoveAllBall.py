class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        answer = [0] * n
        count = 0  
        ops = 0    
        for i in range(n):
            answer[i] += ops
            count += int(boxes[i])
            ops += count
        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += ops
            count += int(boxes[i])
            ops += count
        
        return answer

def run_test_cases():
    solution = Solution()
    
    test_cases = [
        ("110", [1, 1, 3]),
        ("001011", [11, 8, 5, 4, 3, 4]),
        ("0", [0]),  # Single box, empty
        ("1", [0]),  # Single box, full
        ("0000", [0, 0, 0, 0]),  # All boxes empty
        ("1111", [6, 4, 4, 6]),  # All boxes full
        ("1010", [4, 2, 4, 6]),  # Alternate empty and full boxes
    ]
    
    for i, (boxes, expected) in enumerate(test_cases, 1):
        output = solution.minOperations(boxes)
        print(f"Test case {i}: Input: {boxes}")
        print(f"Expected Output: {expected}")
        print(f"Actual Output:   {output}")
        print(f"Result: {'PASS' if output == expected else 'FAIL'}\n")

if __name__ == "__main__":
    run_test_cases()