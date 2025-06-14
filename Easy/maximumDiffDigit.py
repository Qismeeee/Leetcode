class Solution(object):
    def minMaxDifference(self, num):
        s = str(num)
        max_v = 0
        min_v = float('inf')
        for d1 in '0123456789':
            for d2 in '0123456789':
                t = s.replace(d1, d2)
                val = int(t)
                if val > max_v:
                    max_v = val
                if val < min_v:
                    min_v = val
        return max_v - min_v

if __name__ == "__main__":
    tests = [
        (11891, 99009),
        (90, 99),
        (12345, 86424),
        (1000, 9000),
        (5, 8)
    ]
    for num, expected in tests:
        result = Solution().minMaxDifference(num)
        print(result, expected, 'PASS' if result == expected else 'FAIL')