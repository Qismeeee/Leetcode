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

def run_tests():
    s = Solution()
    cases = [
        ("1.2", "1.10", -1),
        ("1.01", "1.001", 0),
        ("1.0", "1.0.0.0", 0),
        ("0.1", "1.0", -1),
        ("1.0.1", "1", 1),
        ("7.5.2.4", "7.5.3", -1),
        ("3.10.0", "3.2.9", 1),
        ("0001.000", "1", 0),
        ("1.0.0.0.0.0.1", "1", 1),
        ("2.0", "2.0.0", 0),
    ]
    for v1, v2, expected in cases:
        out = s.compareVersion(v1, v2)
        assert out == expected, f"{v1} vs {v2}: expected {expected}, got {out}"
        print(f"{v1} ? {v2} -> {out}")

run_tests()
