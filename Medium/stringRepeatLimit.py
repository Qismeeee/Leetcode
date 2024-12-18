from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        char_count = Counter(s)
        max_heap = []
        
        for char, count in char_count.items():
            heapq.heappush(max_heap, (-ord(char), char, count))
        
        result = []
        
        while max_heap:
            _, char, count = heapq.heappop(max_heap)
            add_count = min(count, repeatLimit)
            result.extend([char] * add_count)
            count -= add_count
            
            if count > 0:
                if not max_heap:
                    break  
                
                _, next_char, next_count = heapq.heappop(max_heap)
                result.append(next_char)
                next_count -= 1
                
                if next_count > 0:
                    heapq.heappush(max_heap, (-ord(next_char), next_char, next_count))
                heapq.heappush(max_heap, (-ord(char), char, count))
        
        return ''.join(result)


s = "cczazcc"
repeatLimit = 3
solution = Solution()
print(solution.repeatLimitedString(s, repeatLimit))  
