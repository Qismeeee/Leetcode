class Solution(object):
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        for i in range(n):
            for j in range(i + 1, n - (i + 1)):
                fruits[i][j] = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], fruits[i - 1][j], fruits[i - 1][j + 1] if j + 1 < n else 0
                )
        for j in range(n):
            for i in range(j + 1, n - (j + 1)):
                fruits[i][j] = 0
        for j in range(1, n - 1):
            for i in range(j + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], fruits[i][j - 1], fruits[i + 1][j - 1] if i + 1 < n else 0
                )
        return sum(fruits[i][i] for i in range(n)) + fruits[-2][-1] + fruits[-1][-2]


sol = Solution()

test_cases = [
    [[3]],
    [[1, 2], [3, 4]],
    [[2, 1, 3], [4, 5, 6], [7, 8, 9]],
]

for idx, case in enumerate(test_cases, 1):
    print(f"Case {idx}:", sol.maxCollectedFruits([row[:] for row in case]))
