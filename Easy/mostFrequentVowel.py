from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        v = set("aeiou")
        cnt = Counter(s)
        mv = mc = 0
        for ch, f in cnt.items():
            if ch in v:
                mv = max(mv, f)
            else:
                mc = max(mc, f)
        return mv + mc

def run_tests():
    s = Solution()
    cases = [
        ("successes", 6),
        ("aeiaeia", 3),
        ("abc", 2),
        ("bcdfg", 1),
        ("uueeii", 2),
        ("zzzza", 5),
        ("a", 1),
        ("q", 1),
    ]
    for inp, expected in cases:
        out = s.maxFreqSum(inp)
        assert out == expected, f"{inp}: expected {expected}, got {out}"
        print(inp, out)

run_tests()
