class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

def test_prefix_count():
    solution = Solution()
    
    # Test case 1
    words1 = ["pay", "attention", "practice", "attend"]
    pref1 = "at"
    assert solution.prefixCount(words1, pref1) == 2, "Test case 1 failed"

    # Test case 2
    words2 = ["leetcode", "win", "loops", "success"]
    pref2 = "code"
    assert solution.prefixCount(words2, pref2) == 0, "Test case 2 failed"

    # Test case 3
    words3 = ["apple", "application", "app", "banana", "apply"]
    pref3 = "app"
    assert solution.prefixCount(words3, pref3) == 3, "Test case 3 failed"

    # Test case 4
    words4 = ["dog", "cat", "fish", "dolphin", "do"]
    pref4 = "do"
    assert solution.prefixCount(words4, pref4) == 2, "Test case 4 failed"

    # Test case 5
    words5 = ["prefix", "pretest", "presume", "present", "postfix"]
    pref5 = "pre"
    assert solution.prefixCount(words5, pref5) == 4, "Test case 5 failed"

    print("All test cases passed!")

test_prefix_count()
