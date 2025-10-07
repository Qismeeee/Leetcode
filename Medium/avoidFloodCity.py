import bisect

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n              
        dry_days = []                
        last = {}                    
        for i, lake in enumerate(rains):
            if lake == 0:
                ans[i] = 1
                bisect.insort(dry_days, i)
            else:
                if lake in last:
                    j = bisect.bisect_right(dry_days, last[lake])
                    if j == len(dry_days):
                        return []
                    dry_idx = dry_days.pop(j)      
                    ans[dry_idx] = lake
                last[lake] = i
                ans[i] = -1                      
        return ans

rains = [1,2,0,0,2,1]
s = Solution()
print(s.avoidFlood(rains))
