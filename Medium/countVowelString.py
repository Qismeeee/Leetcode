class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        is_vowel_word = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        prefix_sum = [0] * (len(words) + 1)
        for i in range(len(words)):
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_word[i]
        ans = []
        for li, ri in queries:
            ans.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return ans
    

def test_vowelStrings():
    solution = Solution()
    
    # Test case 1
    words1 = ["aba", "bcb", "ece", "aa", "e"]
    queries1 = [[0, 2], [1, 4], [1, 1]]
    assert solution.vowelStrings(words1, queries1) == [2, 3, 0]
    
    # Test case 2
    words2 = ["a", "e", "i"]
    queries2 = [[0, 2], [0, 1], [2, 2]]
    assert solution.vowelStrings(words2, queries2) == [3, 2, 1]
    
    # Test case 3
    words3 = ["abc", "iou", "xyx", "ue"]
    queries3 = [[0, 3], [1, 2], [1, 1]]
    assert solution.vowelStrings(words3, queries3) == [2, 1, 1]
    
    print("All test cases passed!")

test_vowelStrings()