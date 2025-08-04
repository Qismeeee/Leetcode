class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if not fruits:
            return 0
        fruit_count = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
    

def test_solution():
    sol = Solution()
    
    # Test case 1: [1,2,1] -> 3
    fruits1 = [1,2,1]
    result1 = sol.totalFruit(fruits1)
    print(f"Test 1: {result1} (expected: 3)")
    
    # Test case 2: [0,1,2,2] -> 3
    fruits2 = [0,1,2,2]
    result2 = sol.totalFruit(fruits2)
    print(f"Test 2: {result2} (expected: 3)")
    
    # Test case 3: [1,2,3,2,2] -> 4
    fruits3 = [1,2,3,2,2]
    result3 = sol.totalFruit(fruits3)
    print(f"Test 3: {result3} (expected: 4)")
    
    # Additional test cases
    fruits4 = [3,3,3,1,2,1,1,2,3,3,4]
    result4 = sol.totalFruit(fruits4)
    print(f"Test 4: {result4}")
    
    fruits5 = [1,1,1,1]
    result5 = sol.totalFruit(fruits5)
    print(f"Test 5: {result5}")
    
    fruits6 = [1,2,3,4,5]
    result6 = sol.totalFruit(fruits6)
    print(f"Test 6: {result6}")

test_solution()