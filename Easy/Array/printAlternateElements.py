class Solution:
    def getAlternates(self, arr):
        res = []
        for i in range(len(arr)):
            if i % 2 == 0:
                res.append(arr[i])
        return res

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")

