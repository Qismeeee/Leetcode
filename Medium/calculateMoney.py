class Solution(object):
    def totalMoney(self, n):
        ans = 0
        deposit = 1
        day_in_week = 0
        for _ in range(n):
            ans += deposit
            deposit += 1
            day_in_week += 1
            if day_in_week == 7:
                day_in_week = 0
                deposit -= 6
        return ans

n = 4
s = Solution()
print(s.totalMoney(n))  # 10

n = 10
print(s.totalMoney(n))  # 37

n = 20
print(s.totalMoney(n))  # 96
