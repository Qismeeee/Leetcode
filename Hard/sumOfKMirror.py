class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def to_base_k(num, base):
            """Convert number to base-k representation"""
            if num == 0:
                return "0"
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))
        
        def is_palindrome(s):
            """Check if string is a palindrome"""
            return s == s[::-1]
        
        def generate_palindromes():
            """Generator that yields palindromes in increasing order"""
            for i in range(1, 10):
                yield i
            
            length = 2
            while True:
                if length % 2 == 0:
                    half_length = length // 2
                    start = 10 ** (half_length - 1)
                    end = 10 ** half_length
                    
                    for i in range(start, end):
                        s = str(i)
                        palindrome = int(s + s[::-1])
                        yield palindrome
                else:
                    half_length = (length - 1) // 2
                    if half_length > 0:
                        start = 10 ** (half_length - 1)
                        end = 10 ** half_length
                        
                        for i in range(start, end):
                            s = str(i)
                            for mid_digit in range(10):
                                palindrome = int(s + str(mid_digit) + s[::-1])
                                yield palindrome
                
                length += 1
        
        result = []
        for palindrome in generate_palindromes():
            base_k_repr = to_base_k(palindrome, k)
            if is_palindrome(base_k_repr):
                result.append(palindrome)
                if len(result) == n:
                    break
        
        return sum(result)

def test_solution():
    sol = Solution()
    result1 = sol.kMirror(2, 5)
    print(f"Example 1 (k=2, n=5): {result1}")  
    result2 = sol.kMirror(3, 7)
    print(f"Example 2 (k=3, n=7): {result2}")  
    result3 = sol.kMirror(5, 20)
    print(f"Test case (k=5, n=20): {result3}")

test_solution()