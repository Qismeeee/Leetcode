class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        b = set(brokenLetters)
        return sum(1 for w in text.split() if set(w).isdisjoint(b))


def run_tests():
    s = Solution()
    cases = [
        ("hello world", "ad", 1),
        ("leet code", "lt", 1),
        ("leet code", "e", 0),
        ("a b c", "", 3),
        ("a b c", "abc", 0),
        ("abc def", "x", 2),
        ("aaaa bbbb cccc", "ab", 0),
        ("type fast", "yz", 2),
    ]
    for text, broken, expected in cases:
        out = s.canBeTypedWords(text, broken)
        assert out == expected, f"{text},{broken}: expected {expected}, got {out}"
        print((text, broken), out)

run_tests()
