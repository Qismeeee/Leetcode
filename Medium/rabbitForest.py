class Solution(object):
    def numRabbits(self, answers):
        count = {}
        for answer in answers:
            count[answer] = count.get(answer, 0) + 1
        result = 0
        for answer, c in count.items():
            result += ((c + answer) // (answer + 1)) * (answer + 1)
        return result


s = Solution()
print(s.numRabbits([1, 1, 2]))
print(s.numRabbits([10, 10, 10]))
print(s.numRabbits([0]))
print(s.numRabbits([1, 0, 1]))
print(s.numRabbits([0, 0, 0]))
