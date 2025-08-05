class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        available_baskets = baskets[:]  
        used_baskets = [False] * len(baskets)  
        unplaced_count = 0
        
        for fruit_quantity in fruits:
            placed = False
            for i in range(len(available_baskets)):
                if not used_baskets[i] and available_baskets[i] >= fruit_quantity:
                    used_baskets[i] = True
                    placed = True
                    break
            
            if not placed:
                unplaced_count += 1
        
        return unplaced_count

def test_solution():
    sol = Solution()
    
    # Test case 1: fruits = [4,2,5], baskets = [3,5,4] -> 1
    fruits1 = [4,2,5]
    baskets1 = [3,5,4]
    result1 = sol.numOfUnplacedFruits(fruits1, baskets1)
    print(f"Test 1: {result1} (expected: 1)")
    print(f"  fruits[0]=4 -> baskets[1]=5 ✓")
    print(f"  fruits[1]=2 -> baskets[0]=3 ✓") 
    print(f"  fruits[2]=5 -> baskets[2]=4 ✗ (insufficient capacity)")
    print()
    
    # Test case 2: fruits = [3,6,1], baskets = [6,4,7] -> 0
    fruits2 = [3,6,1]
    baskets2 = [6,4,7]
    result2 = sol.numOfUnplacedFruits(fruits2, baskets2)
    print(f"Test 2: {result2} (expected: 0)")
    print(f"  fruits[0]=3 -> baskets[0]=6 ✓")
    print(f"  fruits[1]=6 -> baskets[1]=4 ✗, baskets[2]=7 ✓")
    print(f"  fruits[2]=1 -> baskets[1]=4 ✓")
    print()
    
    # Additional test cases
    fruits3 = [5,5,5]
    baskets3 = [3,3,3]
    result3 = sol.numOfUnplacedFruits(fruits3, baskets3)
    print(f"Test 3: {result3} (expected: 3 - all fruits too big)")
    
    fruits4 = [1,2,3]
    baskets4 = [3,2,1]
    result4 = sol.numOfUnplacedFruits(fruits4, baskets4)
    print(f"Test 4: {result4} (expected: 1)")
    print(f"  fruits[0]=1 -> baskets[0]=3 ✓")
    print(f"  fruits[1]=2 -> baskets[1]=2 ✓")
    print(f"  fruits[2]=3 -> baskets[2]=1 ✗ (insufficient capacity)")
    
    fruits5 = [1,1,1]
    baskets5 = [5,5,5]
    result5 = sol.numOfUnplacedFruits(fruits5, baskets5)
    print(f"Test 5: {result5} (expected: 0 - all fruits fit)")

test_solution()