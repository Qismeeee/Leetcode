import bisect


class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        end_times = []
        max_value_up_to = []

        result = 0
        max_value = 0

        for start, end, value in events:
            idx = bisect.bisect_right(end_times, start - 1)
            if idx > 0:
                result = max(result, value + max_value_up_to[idx - 1])

            result = max(result, value)
            max_value = max(max_value, value)
            end_times.append(end)
            max_value_up_to.append(max_value)

        return result


solution = Solution()

# Test Case 1
events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
print(solution.maxTwoEvents(events))  

# Test Case 2
events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
print(solution.maxTwoEvents(events))  

# Test Case 3
events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
print(solution.maxTwoEvents(events)) 

# Test Case 4
events = [[10, 83, 53], [63, 87, 45], [97, 100, 32], [51, 61, 16]]
print(solution.maxTwoEvents(events))  

# Test Case 5
events = [[1, 10, 5], [11, 20, 10], [21, 30, 15]]
print(solution.maxTwoEvents(events))  
