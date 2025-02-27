class Solution(object):
    def lenLongestFibSubseq(self, arr):
        index_map = {num: idx for idx, num in enumerate(arr)}

        dp = {}
        max_len = 0
        
        for j in range(1, len(arr)):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev < arr[i] and prev in index_map:  
                    k = index_map[prev]
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[(i, j)])
        return max_len if max_len >= 3 else 0


# Test case 1:
arr = [1, 2, 3, 4, 5, 6, 7, 8]
solution = Solution()
print(solution.lenLongestFibSubseq(arr))  

# Test case 2:
arr = [1, 3, 7, 11, 12, 14, 18]
solution = Solution()
print(solution.lenLongestFibSubseq(arr))  

# Test case 3 (Edge case):
arr = [1, 3, 7]
solution = Solution()
print(solution.lenLongestFibSubseq(arr)) 

# Test case 4 (No valid Fibonacci subsequence):
arr = [1, 2, 4, 5, 10]
solution = Solution()
print(solution.lenLongestFibSubseq(arr)) 
