class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_question = min(n, i + brainpower + 1)
            dp[i] = max(dp[i+1], points + dp[next_question])
        
        return dp[0]

def debug_solution():
    solution = Solution()
    
    test_cases = [
        [[3,2],[4,3],[4,4],[2,5]],
        [[1,1],[2,2],[3,3],[4,4],[5,5]],
        [[1,1]],
        [[1,2],[2,1]],
        [[3,2],[4,3],[4,4],[2,5],[1,1]]
    ]
    
    for i, case in enumerate(test_cases, 1):
        result = solution.mostPoints(case)
        print(f"Test Case {i}: {case}")
        print(f"Result: {result}\n")

debug_solution()