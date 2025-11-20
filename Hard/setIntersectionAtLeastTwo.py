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
