class Solution:
    def putMarbles(self, weights, k):
        if k == 1 or k == len(weights):
            return 0
        pair_sums = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
        pair_sums.sort()
        return sum(pair_sums[-(k-1):]) - sum(pair_sums[:k-1])
    
def test_put_marbles():
    solution = Solution()
    weights1 = [1, 3, 5, 1]
    k1 = 2
    result1 = solution.putMarbles(weights1, k1)
    print(f"Test case 1: {result1}")
    
    weights2 = [1, 3]
    k2 = 2
    result2 = solution.putMarbles(weights2, k2)
    print(f"Test case 2: {result2}")

test_put_marbles()