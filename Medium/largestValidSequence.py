class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        
        def backtrack(index):
            if index == len(result):
                return True
            
            if result[index] != 0:
                return backtrack(index + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    result[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[1] = False
                    continue
                
                target_index = index + num
                if target_index < len(result) and result[target_index] == 0:
                    result[index] = num
                    result[target_index] = num
            
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    result[target_index] = 0
                    used[num] = False
            
            return False

        backtrack(0)
        return result
    
def test_distant_sequence():
    sol = Solution()
    
    # Test case 1: n = 3
    assert sol.constructDistancedSequence(3) == [3,1,2,3,2], "Test case 1 failed"
    
    # Test case 2: n = 5
    assert sol.constructDistancedSequence(5) == [5,3,1,4,3,5,2,4,2], "Test case 2 failed"
    
    # Test case 3: n = 1
    assert sol.constructDistancedSequence(1) == [1], "Test case 3 failed"
    
    # Test case 4: n = 2
    assert sol.constructDistancedSequence(2) == [2,1,2], "Test case 4 failed"
    
    # Test case 5: n = 4
    result = sol.constructDistancedSequence(4)
    # Verify the constraints manually
    assert len(result) == 2 * 4 - 1, "Test case 5 length incorrect"
    assert result.count(1) == 1, "Test case 5 should have exactly one 1"
    
    print("All test cases passed!")

test_distant_sequence()