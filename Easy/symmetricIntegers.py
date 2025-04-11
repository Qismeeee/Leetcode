class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for num in range(low, high + 1):
            str_num = str(num)
            n = len(str_num)
            if n % 2 == 0:
                half = n // 2
                first_half = str_num[:half]
                second_half = str_num[half:]
                sum_first_half = sum(int(digit) for digit in first_half)
                sum_second_half = sum(int(digit) for digit in second_half)
                
                if sum_first_half == sum_second_half:
                    count += 1
        
        return count

solution = Solution()
print(solution.countSymmetricIntegers(1, 100)) 
print(solution.countSymmetricIntegers(1200, 1230))