class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_val = -1  
        chunks = 0    
        
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            
            if max_val == i:
                chunks += 1
        
        return chunks


test_cases = [
    ([4, 3, 2, 1, 0], 1),  
    ([1, 0, 2, 3, 4], 4), 
    ([0, 1, 2, 3, 4], 5),  
    ([2, 0, 1, 4, 3], 1),  
    ([1, 0], 1),           
]

def test_solution():
    solution = Solution()
    for i, (arr, expected) in enumerate(test_cases):
        result = solution.maxChunksToSorted(arr)
        print(f"Test case {i + 1}: {'Pass' if result == expected else 'Fail'}")
        print(f"  Input: {arr}")
        print(f"  Expected: {expected}, Got: {result}\n")

# Chạy kiểm tra
test_solution()