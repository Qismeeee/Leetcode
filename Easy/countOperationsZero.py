class Solution(object):
    def countOperations(self, num1, num2):
        cnt = 0
        while num1 and num2:
            if num1 >= num2:
                cnt += num1 // num2
                num1 %= num2
            else:
                cnt += num2 // num1
                num2 %= num1
        return cnt

s = Solution()
print(s.countOperations(2, 3))   # 3
print(s.countOperations(10, 10)) # 1
print(s.countOperations(0, 5))   # 0
print(s.countOperations(7, 4))   # 3
