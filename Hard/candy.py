class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 4, 5, 2], 11),
        ([1], 1),
        ([2, 2, 2], 3)
    ]
    for ratings, expected in tests:
        result = sol.candy(ratings)
        print(result == expected, result)
