class Solution:
    def countGoodStrings(self, low, high, zero, one):
        MOD = 10**9 + 7
        
        dp = [0] * (high + 1)
        dp[0] = 1 
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        
        return sum(dp[low:high + 1]) % MOD
    

solution = Solution()
test_cases = [
    {"low": 3, "high": 3, "zero": 1, "one": 1, "expected": 8},
    {"low": 2, "high": 3, "zero": 1, "one": 2, "expected": 5},
    {"low": 1, "high": 5, "zero": 1, "one": 1, "expected": 16},
    {"low": 5, "high": 10, "zero": 2, "one": 3, "expected": 27},
    {"low": 1, "high": 1, "zero": 1, "one": 2, "expected": 1},
]

for idx, test in enumerate(test_cases):
    result = solution.countGoodStrings(test["low"], test["high"], test["zero"], test["one"])
    print(f"Test case {idx + 1}: ", "Passed" if result == test["expected"] else f"Failed (Expected: {test['expected']}, Got: {result})")