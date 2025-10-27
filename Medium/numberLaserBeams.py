class Solution(object):
    def numberOfBeams(self, bank):
        prev = 0
        ans = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                ans += prev * cnt
                prev = cnt
        return ans
