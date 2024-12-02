"""Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s."""

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for index, word in enumerate(words):
            if (word.startswith(searchWord)):
                return index + 1

        return -1

solution = Solution()

sentence = "this problem is an easy problem"
searchWord = "you"
results = solution.isPrefixOfWord(sentence, searchWord)
print(results)