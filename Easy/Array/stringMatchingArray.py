class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break  
        return result


def test_solution():
    # Test Case 1
    words1 = ["mass", "as", "hero", "superhero"]
    expected1 = ["as", "hero"]
    solution = Solution()
    result1 = solution.stringMatching(words1)
    print(f"Test Case 1: {result1}")
    assert sorted(result1) == sorted(expected1), f"Expected {expected1}, but got {result1}"

    # Test Case 2
    words2 = ["leetcode", "et", "code"]
    expected2 = ["et", "code"]
    result2 = solution.stringMatching(words2)
    print(f"Test Case 2: {result2}")
    assert sorted(result2) == sorted(expected2), f"Expected {expected2}, but got {result2}"

    # Test Case 3
    words3 = ["blue", "green", "bu"]
    expected3 = []
    result3 = solution.stringMatching(words3)
    print(f"Test Case 3: {result3}")
    assert result3 == expected3, f"Expected {expected3}, but got {result3}"

    # Test Case 4: Only one word in the list
    words4 = ["hello"]
    expected4 = []
    result4 = solution.stringMatching(words4)
    print(f"Test Case 4: {result4}")
    assert result4 == expected4, f"Expected {expected4}, but got {result4}"

    # Test Case 5: All words are substrings
    words5 = ["a", "ab", "abc", "abcd"]
    expected5 = ["a", "ab", "abc"]
    result5 = solution.stringMatching(words5)
    print(f"Test Case 5: {result5}")
    assert sorted(result5) == sorted(expected5), f"Expected {expected5}, but got {result5}"

    # Test Case 6: No substrings
    words6 = ["apple", "banana", "cherry"]
    expected6 = []
    result6 = solution.stringMatching(words6)
    print(f"Test Case 6: {result6}")
    assert result6 == expected6, f"Expected {expected6}, but got {result6}"

   # Test Case 7: Long words with substring
    words7 = ["supercalifragilisticexpialidocious", "fragile", "super", "frag"]
    expected7 = ["super", "frag"]  # Corrected expected result
    result7 = solution.stringMatching(words7)
    print(f"Test Case 7: {result7}")
    assert sorted(result7) == sorted(expected7), f"Expected {expected7}, but got {result7}"


test_solution()
