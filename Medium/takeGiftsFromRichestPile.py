import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)  

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            remaining = int(math.sqrt(largest))  
            heapq.heappush(max_heap, -remaining)

        return -sum(max_heap)
    

solution = Solution()
print(solution.pickGifts([25, 64, 9, 4, 100], 4)) 
print(solution.pickGifts([1, 1, 1, 1], 4))        
