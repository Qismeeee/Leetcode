class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        merged = []
        
        for start, end in meetings:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        booked_days = 0
        for start, end in merged:
            booked_days += end - start + 1
        available_days = days - booked_days
        
        return available_days


solution = Solution()
# Test case 1
days = 10
meetings = [[5,7],[1,3],[9,10]]
print(solution.countDays(days, meetings)) 

# Test case 2
days = 5
meetings = [[2,4],[1,3]]
print(solution.countDays(days, meetings))  

# Test case 3
days = 6
meetings = [[1,6]]
print(solution.countDays(days, meetings))  

# Test case 4
days = 7
meetings = [[1,2], [4,5], [6,7]]
print(solution.countDays(days, meetings))  

# Test case 5
days = 15
meetings = [[3,6], [7,9], [12,15]]
print(solution.countDays(days, meetings))  
