from typing import List
import math

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        blockSize = math.floor(math.sqrt(n))
        blocks = []

        for i in range(0, n, blockSize):
            end = min(i + blockSize, n)
            maxInBlock = -1
            for j in range(i, end):
                if baskets[j] > maxInBlock:
                    maxInBlock = baskets[j]
            blocks.append(maxInBlock)
        
        count = 0
        for fruit in fruits:
            basketFound = False
            for i in range(len(blocks)):
                if (blocks[i] >= fruit):
                    start = i * blockSize
                    end = min(start + blockSize, n)

                    for j in range(start, end):
                        if baskets[j] >= fruit:
                            baskets[j] = -1
                            basketFound = True

                            newMax = -1
                            for k in range(start, end):
                                if (baskets[k] > newMax):
                                    newMax = baskets[k]
                            blocks[i] = newMax
                            break
                if basketFound:
                    break
            if not basketFound:
                count += 1
        return count
    
def test_solution():
    sol = Solution()
    
    # Test case 1: fruits = [4,2,5], baskets = [3,5,4] -> 1
    fruits1 = [4,2,5]
    baskets1 = [3,5,4]
    result1 = sol.numOfUnplacedFruits(fruits1, baskets1)
    print(f"Test 1: {result1} (expected: 1)")
    
    # Test case 2: fruits = [3,6,1], baskets = [6,4,7] -> 0  
    fruits2 = [3,6,1]
    baskets2 = [6,4,7]
    result2 = sol.numOfUnplacedFruits(fruits2, baskets2)
    print(f"Test 2: {result2} (expected: 0)")
    
    # Test larger input
    fruits3 = list(range(1000, 0, -1))  
    baskets3 = list(range(1, 1001))    
    result3 = sol.numOfUnplacedFruits(fruits3, baskets3)
    print(f"Test 3 (large): {result3}")
    
    # Test all fruits too big
    fruits4 = [10, 10, 10]
    baskets4 = [5, 5, 5]
    result4 = sol.numOfUnplacedFruits(fruits4, baskets4)
    print(f"Test 4: {result4} (expected: 3)")

test_solution()