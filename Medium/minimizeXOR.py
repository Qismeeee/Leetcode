class Solution(object):
    def minimizeXor(self, num1, num2):
        num2_bits = bin(num2).count('1')
        set_bits_num1 = []
        for i in range(32):  
            if num1 & (1 << i):
                set_bits_num1.append(i)
        
        x = 0
        set_bits_used = 0
        for i in set_bits_num1:
            if set_bits_used < num2_bits:
                x |= (1 << i)  
                set_bits_used += 1
        i = 0
        while set_bits_used < num2_bits:
            if not (x & (1 << i)):  
                x |= (1 << i)  
                set_bits_used += 1
            i += 1
        
        return x

def test_minimizeXor():
    solution = Solution()
    # Test case 1: num1 = 3, num2 = 5
    num1 = 3
    num2 = 5
    result = solution.minimizeXor(num1, num2)
    print(f"Test case 1: num1 = {num1}, num2 = {num2} => Result: {result}")

    # Test case 2: num1 = 1, num2 = 12
    num1 = 1
    num2 = 12
    result = solution.minimizeXor(num1, num2)
    print(f"Test case 2: num1 = {num1}, num2 = {num2} => Result: {result}")

    # Test case 3: num1 = 7, num2 = 14
    num1 = 7
    num2 = 14
    result = solution.minimizeXor(num1, num2)
    print(f"Test case 3: num1 = {num1}, num2 = {num2} => Result: {result}")

    # Test case 4: num1 = 10, num2 = 7
    num1 = 10
    num2 = 7
    result = solution.minimizeXor(num1, num2)
    print(f"Test case 4: num1 = {num1}, num2 = {num2} => Result: {result}")

    # Test case 5: num1 = 0, num2 = 15
    num1 = 0
    num2 = 15
    result = solution.minimizeXor(num1, num2)
    print(f"Test case 5: num1 = {num1}, num2 = {num2} => Result: {result}")

test_minimizeXor()
