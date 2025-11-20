class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        last1 = -1
        last2 = -1
        ans = 0

        for s, e in intervals:
            if s <= last2:
                continue
            elif s > last1:
                ans += 2
                last2 = e - 1
                last1 = e
            else:
                ans += 1
                last2 = last1
                last1 = e

        return ans


s = Solution()

print(s.intersectionSizeTwo([[1,3],[3,7],[8,9]]))          # 5
print(s.intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))    # 3
print(s.intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))    # 5
