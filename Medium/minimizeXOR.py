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
