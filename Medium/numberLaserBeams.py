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

bank = ["011001","000000","010100","001000"]
s = Solution()
print(s.numberOfBeams(bank))  # 8

bank = ["000","111","000"]
print(s.numberOfBeams(bank))  # 0

bank = ["1","0","1"]
print(s.numberOfBeams(bank))  # 1
