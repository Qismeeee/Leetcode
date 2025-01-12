class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False  
        
        open_balance = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                open_balance += 1
            else:
                open_balance -= 1
            if open_balance < 0:
                return False  
        close_balance = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_balance += 1
            else:
                close_balance -= 1
            if close_balance < 0:
                return False 
        
        return True

def test_canBeValid():
    solution = Solution()

    # Test case 1
    s = "))()))"
    locked = "010100"
    assert solution.canBeValid(s, locked) == True, "Test case 1 failed"

    # Test case 2
    s = "()()"
    locked = "0000"
    assert solution.canBeValid(s, locked) == True, "Test case 2 failed"

    # Test case 3
    s = ")"
    locked = "0"
    assert solution.canBeValid(s, locked) == False, "Test case 3 failed"

    # Test case 4: Already valid parentheses string
    s = "((()))"
    locked = "111111"
    assert solution.canBeValid(s, locked) == True, "Test case 4 failed"

    # Test case 5: Fully unlocked, odd length
    s = "(()"
    locked = "000"
    assert solution.canBeValid(s, locked) == False, "Test case 5 failed"

    # Test case 6: Fully unlocked, even length
    s = "(())"
    locked = "0000"
    assert solution.canBeValid(s, locked) == True, "Test case 6 failed"

    # Test case 7: Locked invalid string
    s = "())("
    locked = "1111"
    assert solution.canBeValid(s, locked) == False, "Test case 7 failed"

    # Test case 8: Large valid string
    s = "()" * 5000
    locked = "0" * 10000
    assert solution.canBeValid(s, locked) == True, "Test case 8 failed"

    print("All test cases passed!")

test_canBeValid()
