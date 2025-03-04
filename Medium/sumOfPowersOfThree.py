class Solution(object):
    def checkPowersOfThree(self, n):
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

    

def test_checkPowersOfThree():
    solution = Solution()
    
    assert solution.checkPowersOfThree(12) == True
    assert solution.checkPowersOfThree(91) == True
    assert solution.checkPowersOfThree(21) == False
    assert solution.checkPowersOfThree(1) == True
    assert solution.checkPowersOfThree(3) == True
    assert solution.checkPowersOfThree(10) == False
    assert solution.checkPowersOfThree(27) == True
    assert solution.checkPowersOfThree(40) == False
    print("All test cases passed.")

test_checkPowersOfThree()

