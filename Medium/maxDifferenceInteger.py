class Solution(object):
    def maxDiff(self, num):
        s = str(num)
        # maximize a
        a = s
        for c in s:
            if c != '9':
                a = s.replace(c, '9')
                break
        # minimize b
        b = s
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for c in s[1:]:
                if c not in ('0', '1'):
                    b = s.replace(c, '0')
                    break
        return int(a) - int(b)