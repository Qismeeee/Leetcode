class Solution(object):
    def getHappyString(self, n, k):
        def dfs(current):
            if len(current) == n:
                happy_strings.append(current)
                return
            for ch in 'abc':
                if not current or current[-1] != ch:
                    dfs(current + ch)
        
        happy_strings = []
        dfs("")
        
        if k <= len(happy_strings):
            return happy_strings[k-1]
        else:
            return ""


def test_getHappyString():
    solution = Solution()

    # Test Case 1: n = 1, k = 3
    print(solution.getHappyString(1, 3)) 

    # Test Case 2: n = 1, k = 4
    print(solution.getHappyString(1, 4))  

    # Test Case 3: n = 3, k = 9
    print(solution.getHappyString(3, 9)) 

    # Test Case 4: n = 2, k = 5
    print(solution.getHappyString(2, 5)) 

    # Test Case 5: n = 3, k = 1
    print(solution.getHappyString(3, 1)) 



test_getHappyString()
