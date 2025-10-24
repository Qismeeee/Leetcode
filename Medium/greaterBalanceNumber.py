class Solution(object):
    def nextBeautifulNumber(self, n):
        def good(x):
            s = str(x)
            cnt = [0]*10
            for ch in s:
                d = ord(ch) - 48
                if d == 0:
                    return False
                cnt[d] += 1
            for d in range(1,10):
                if cnt[d] != 0 and cnt[d] != d:
                    return False
            return True

        cur = n + 1
        while True:
            if good(cur):
                return cur
            cur += 1
n = 1
s = Solution()
print(s.nextBeautifulNumber(n))  # 22

n = 1000
print(s.nextBeautifulNumber(n))  # 1333

n = 3000
print(s.nextBeautifulNumber(n))  # 3133
