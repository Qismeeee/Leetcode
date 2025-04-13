class Solution:
    MOD = 10**9 + 7

    def modExp(self, base, exp):
        result = 1
        base %= self.MOD
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            exp //= 2
        return result

    def countGoodNumbers(self, n):
        evens = (n + 1) // 2
        odds = n // 2
        evenPart = self.modExp(5, evens)
        oddPart = self.modExp(4, odds)
        return (evenPart * oddPart) % self.MOD
    

solution = Solution()
# Test Case 1
print(solution.countGoodNumbers(1)) 

# Test Case 2
print(solution.countGoodNumbers(4)) 

# Test Case 3
print(solution.countGoodNumbers(2)) 

# Test Case 4
print(solution.countGoodNumbers(3)) 

# Test Case 5
print(solution.countGoodNumbers(5)) 
