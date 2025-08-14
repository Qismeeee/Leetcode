class Solution(object):
    def largestGoodInteger(self, num):
        for d in "9876543210":
            t = d * 3
            if t in num:
                return t
        return ""
