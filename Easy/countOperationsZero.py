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
