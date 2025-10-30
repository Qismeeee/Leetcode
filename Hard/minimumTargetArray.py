class Solution(object):
    def minNumberOperations(self, target):
        ans = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                ans += target[i] - target[i-1]
        return ans
s = Solution()
print(s.minNumberOperations([1,2,3,2,1]))
print(s.minNumberOperations([3,1,1,2]))
print(s.minNumberOperations([3,1,5,4,2]))
