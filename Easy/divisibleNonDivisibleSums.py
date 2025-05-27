class Solution(object):
    def differenceOfSums(self, n, m):
        total = n * (n + 1) // 2
        k = n // m
        divisible_sum = m * k * (k + 1) // 2
        return total - 2 * divisible_sum

if __name__ == "__main__":
    print(Solution().differenceOfSums(10, 3))  
    print(Solution().differenceOfSums(5, 6))   
    print(Solution().differenceOfSums(5, 1))