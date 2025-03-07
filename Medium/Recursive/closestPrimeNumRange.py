class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  
        
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        
        primes_in_range = [i for i in range(left, right + 1) if sieve[i]]
        if len(primes_in_range) < 2:
            return [-1, -1]
        min_diff = float('inf')
        result = [-1, -1]
        
        for i in range(len(primes_in_range) - 1):
            num1, num2 = primes_in_range[i], primes_in_range[i + 1]
            if num2 - num1 < min_diff:
                min_diff = num2 - num1
                result = [num1, num2]
        
        return result


# Test case 1: Input với primes trong phạm vi nhỏ
sol = Solution()
print(sol.closestPrimes(10, 19))

# Test case 2: Không có đủ 2 số nguyên tố trong phạm vi
print(sol.closestPrimes(4, 6))    

# Test case 3: Phạm vi từ 1 đến 10, với primes là [2, 3, 5, 7]
print(sol.closestPrimes(1, 10))   

# Test case 4: Phạm vi với chỉ một số nguyên tố
print(sol.closestPrimes(1, 2))    

# Test case 5: Phạm vi có 2 số nguyên tố liên tiếp
print(sol.closestPrimes(3, 5))   
