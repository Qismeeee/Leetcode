class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        def find_prev_non_conflicting(i):
            """Binary search for latest event that doesn't conflict with event i"""
            start = events[i][0]
            left, right = 0, i - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                if events[mid][1] < start:  
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, end, value = events[i-1]
            prev = find_prev_non_conflicting(i-1)
            
            for attended in range(k + 1):
                dp[i][attended] = dp[i-1][attended]
                if attended > 0:
                    prev_value = dp[prev + 1][attended - 1] if prev >= 0 else 0
                    dp[i][attended] = max(dp[i][attended], prev_value + value)
        
        return dp[n][k]
    
def test_solution():
    sol = Solution()
    result1 = sol.maxValue([[1,2,4],[3,4,3],[2,3,1]], 2)
    print(f"Example 1: {result1}") 
    result2 = sol.maxValue([[1,2,4],[3,4,3],[2,3,10]], 2)
    print(f"Example 2: {result2}") 
    result3 = sol.maxValue([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3)
    print(f"Example 3: {result3}")  
    events = [[1,2,4],[3,4,3],[2,3,1]]
    k = 2
    print(f"\nTracing Example 1: events = {events}, k = {k}")
    events.sort(key=lambda x: x[1])
    print(f"Sorted by end time: {events}")
    n = len(events)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    print(f"\nDP table construction:")
    print(f"dp[i][j] = max value using first i events with at most j events")
    
    for i in range(1, n + 1):
        start, end, value = events[i-1]
        print(f"\nProcessing event {i}: [{start},{end},{value}]")
        prev = -1
        for j in range(i-1):
            if events[j][1] < start:
                prev = j
        
        print(f"  Latest non-conflicting event index: {prev}")
        
        for attended in range(k + 1):
            dp[i][attended] = dp[i-1][attended]
            if attended > 0:
                prev_value = dp[prev + 1][attended - 1] if prev >= 0 else 0
                dp[i][attended] = max(dp[i][attended], prev_value + value)
        
        print(f"  DP row {i}: {dp[i]}")
    
    print(f"\nFinal answer: {dp[n][k]}")
    print(f"\nFor Example 1, optimal solution:")
    print(f"Events [1,2,4] and [3,4,3] give value 4+3=7")
    print(f"Event [2,3,10] from Example 2 alone gives value 10")

test_solution()