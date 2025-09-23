class Solution(object):
    def compareVersion(self, version1, version2):
        a = list(map(int, version1.split('.')))
        b = list(map(int, version2.split('.')))
        n = max(len(a), len(b))
        for i in range(n):
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0
            if x < y:
                return -1
            if x > y:
                return 1
        return 0
