class Solution(object):
    def maxDiff(self, num):
        s = str(num)
        a = s
        for c in s:
            if c != '9':
                a = s.replace(c, '9')
                break
        b = s
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for c in s[1:]:
                if c not in ('0', '1'):
                    b = s.replace(c, '0')
                    break
        return int(a) - int(b)

if __name__ == "__main__":
    tests = [
        (555, 888),
        (9, 8),
        (123456, 820000),
        (10000, 80000),
        (111, 888)
    ]
    for num, expected in tests:
        result = Solution().maxDiff(num)
        print(result, expected, 'PASS' if result == expected else 'FAIL')