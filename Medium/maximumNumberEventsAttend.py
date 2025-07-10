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
        day = 1
        
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


def test_solution():
    sol = Solution()
    
    result1 = sol.maxEvents([[1,2],[2,3],[3,4]])
    print(f"Example 1: {result1}")  
    result2 = sol.maxEvents([[1,2],[2,3],[3,4],[1,2]])
    print(f"Example 2: {result2}")  
    events = [[1,2],[2,3],[3,4]]
    print(f"\nTracing Example 1: events = {events}")
    
    events.sort()
    print(f"Sorted events: {events}")
    
    heap = []
    i = 0
    attended = 0
    day = 1
    
    print(f"\nDay-by-day simulation:")
    
    while i < len(events) or heap:
        print(f"\nDay {day}:")
        events_added = []
        while i < len(events) and events[i][0] == day:
            heapq.heappush(heap, events[i][1])
            events_added.append(events[i])
            i += 1
        
        if events_added:
            print(f"  Events starting today: {events_added}")
        
        expired = []
        while heap and heap[0] < day:
            expired.append(heapq.heappop(heap))
        
        if expired:
            print(f"  Expired events (end days): {expired}")
        
        print(f"  Available events (end days): {sorted(heap)}")
        
        if heap:
            attended_event_end = heapq.heappop(heap)
            attended += 1
            print(f"  ✓ Attended event ending on day {attended_event_end}")
        else:
            print(f"  ✗ No events available")
        
        print(f"  Total attended so far: {attended}")
        
        day += 1
        if i >= len(events) and not heap:
            break
    
    print(f"\nFinal result: {attended}")
    print(f"\nAdditional tests:")
    print(f"Single event [[1,1]]: {sol.maxEvents([[1,1]])}")
    print(f"Overlapping [[1,3],[1,3],[1,3]]: {sol.maxEvents([[1,3],[1,3],[1,3]])}")
    print(f"Non-overlapping [[1,1],[2,2],[3,3]]: {sol.maxEvents([[1,1],[2,2],[3,3]])}")

test_solution()