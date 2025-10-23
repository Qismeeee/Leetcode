class Solution(object):
    def hasSameDigits(self, s):
        a = [ord(c) - 48 for c in s]
        while len(a) > 2:
            a = [(a[i] + a[i+1]) % 10 for i in range(len(a)-1)]
        return a[0] == a[1]
