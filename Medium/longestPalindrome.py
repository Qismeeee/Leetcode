from collections import Counter
import unittest

class Solution:
    def longestPalindrome(self, words):
        cnt = Counter(words)
        ans = 0
        center_used = False

        for w, c in cnt.items():
            if w[0] == w[1]:
                pairs = c // 2
                ans += pairs * 4
                if c % 2 == 1 and not center_used:
                    ans += 2
                    center_used = True
            else:
                rev = w[::-1]
                if w < rev and rev in cnt:
                    use = min(c, cnt[rev])
                    ans += use * 4
        return ans

class TestLongestPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(Solution().longestPalindrome(["lc","cl","gg"]), 6)
    def test_example2(self):
        self.assertEqual(Solution().longestPalindrome(["ab","ty","yt","lc","cl","ab"]), 8)
    def test_example3(self):
        self.assertEqual(Solution().longestPalindrome(["cc","ll","xx"]), 2)
    def test_empty(self):
        self.assertEqual(Solution().longestPalindrome([]), 0)
    def test_no_pairs(self):
        self.assertEqual(Solution().longestPalindrome(["ab","cd"]), 0)

if __name__ == "__main__":
    unittest.main()
