from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        arr = [0 for _ in range(2*k+1)]
        for pos, numOfFruit in fruits:
            if pos < startPos-k or pos > startPos+k:
                continue
            arr[pos-(startPos-k)] += numOfFruit
        
        left, right = sum(arr[:k+1]), sum(arr[k:])
        maxSeen = max(left, right)
        
        turn = 1
        for i in range(2, k+1, 2):
            left = left-arr[i-2]-arr[i-1]+arr[k+turn]
            right = right-arr[~(i-2)]-arr[~(i-1)]+arr[k-turn]
            maxSeen = max(maxSeen, left, right)
            turn += 1
        
        return maxSeen

def test_solution():
    sol = Solution()
    
    fruits1 = [[2,8],[6,3],[8,6]]
    result1 = sol.maxTotalFruits(fruits1, 5, 4)
    print(f"Test 1: {result1} (expected: 9)")
    
    fruits2 = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
    result2 = sol.maxTotalFruits(fruits2, 5, 4)
    print(f"Test 2: {result2} (expected: 14)")
    
    fruits3 = [[0,3],[6,4],[8,5]]
    result3 = sol.maxTotalFruits(fruits3, 3, 2)
    print(f"Test 3: {result3} (expected: 0)")
    
    fruits4 = [[200000,10000]]
    result4 = sol.maxTotalFruits(fruits4, 200000, 0)
    print(f"Test 4: {result4} (expected: 10000)")
    
    fruits5 = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    result5 = sol.maxTotalFruits(fruits5, 3, 3)
    print(f"Test 5: {result5}")
    
    fruits6 = [[0,7],[7,4],[9,10],[12,6],[14,9],[16,5]]
    result6 = sol.maxTotalFruits(fruits6, 8, 4)
    print(f"Test 6: {result6}")
    
    fruits7 = [[2,8],[6,3],[8,6]]
    result7 = sol.maxTotalFruits(fruits7, 5, 1)
    print(f"Test 7: {result7}")

test_solution()