import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        
        heap = []  
        i = 0
        attended = 0
        day = events[0][0] if events else 1
        
        while i < len(events) or heap:
            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])  
                i += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                attended += 1
            
            day += 1
        
        return attended