class Solution(object):
    def sortVowels(self, s):
        V = set("aeiouAEIOU")
        vs = sorted([c for c in s if c in V])
        j = 0
        res = []
        for ch in s:
            if ch in V:
                res.append(vs[j])
                j += 1
            else:
                res.append(ch)
        return "".join(res)

def run_tests():
    s = Solution()
    cases = [
        ("lEetcOde", "lEOtcede"),
        ("lYmpH", "lYmpH"),
        ("UoIeA", "AIUeo"),
        ("bAeiDuo", "bAeiDou"),
        ("A", "A"),
        ("bcdfg", "bcdfg"),
        ("aeiouAEIOU", "AEIOUaeiou"),
    ]
    for inp, expected in cases:
        out = s.sortVowels(inp)
        assert out == expected, f"{inp}: expected {expected}, got {out}"
        print(inp, "->", out)

run_tests()
