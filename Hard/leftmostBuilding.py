import bisect

class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        N = len(heights)
        Q = len(queries)
        
        ans = [-1] * Q
        processed_queries = []
        for idx, (ai, bi) in enumerate(queries):
            if ai == bi:
                ans[idx] = ai
            else:
                m = max(ai, bi)
                t = max(heights[ai], heights[bi])
                condition_jm = False
                if m == ai and heights[m] > heights[bi]:
                    condition_jm = True
                elif m == bi and heights[m] > heights[ai]:
                    condition_jm = True
                processed_queries.append( (t, m, idx, condition_jm) )
        
        processed_queries.sort(reverse=True, key=lambda x: x[0])
        sorted_buildings = sorted(range(N), key=lambda j: heights[j], reverse=True)
        sorted_list = []
        
        p = 0
        for t, m, idx, condition_jm in processed_queries:
            while p < N and heights[sorted_buildings[p]] > t:
                j = sorted_buildings[p]
                bisect.insort(sorted_list, j)
                p += 1
            if condition_jm:
                ans[idx] = m
            else:
                pos = bisect.bisect_right(sorted_list, m)
                if pos < len(sorted_list):
                    ans[idx] = sorted_list[pos]
                else:
                    ans[idx] = -1
        return ans


heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]

solution = Solution()
print(solution.leftmostBuildingQueries([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]))
