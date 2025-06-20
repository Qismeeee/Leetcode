import heapq

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        move = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        
        def best_for(sign_x: int, sign_y: int) -> int:
            heap = []     
            sum_gain = 0
            curr = 0      
            best = 0
            for ch in s:
                dx, dy = move[ch]
                cj = sign_x*dx + sign_y*dy
                curr += cj
                dj = 1 - cj
                heapq.heappush(heap, dj)
                sum_gain += dj
                if len(heap) > k:
                    sum_gain -= heapq.heappop(heap)
                best = max(best, curr + sum_gain)
            return best
        
        ans = 0
        for sx, sy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ans = max(ans, best_for(sx, sy))
        return ans