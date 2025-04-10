class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        s_int = int(s)
        s_len = len(s)
        if any(int(digit) > limit for digit in s):
            return 0
        
        def count_up_to(bound):
            bound_str = str(bound)
            bound_len = len(bound_str)
            if bound_len < s_len:
                return 0
            dp = {}
            
            def count_valid_numbers(pos, tight):
                if pos == bound_len:
                    return 1
                key = (pos, tight)
                if key in dp:
                    return dp[key]
                result = 0
                in_suffix = pos >= bound_len - s_len
                
                if in_suffix:
                    s_pos = pos - (bound_len - s_len)
                    s_digit = int(s[s_pos])
                    if tight and s_digit > int(bound_str[pos]):
                        result = 0
                    elif s_digit <= limit:
                        new_tight = tight and s_digit == int(bound_str[pos])
                        result = count_valid_numbers(pos + 1, new_tight)
                else:
                    upper_limit = int(bound_str[pos]) if tight else limit
                    
                    for digit in range(upper_limit + 1):
                        if digit <= limit:
                            new_tight = tight and digit == int(bound_str[pos])
                            result += count_valid_numbers(pos + 1, new_tight)
                
                dp[key] = result
                return result
            
            return count_valid_numbers(0, True)
        return count_up_to(finish) - count_up_to(start - 1)
    

sol = Solution()

test_cases = [
    (1, 6000, 4, "124", 5),
    (15, 215, 6, "10", 2),
    (1000, 2000, 4, "3000", 0),
    (1, 1000, 9, "7", 111),
    (5000, 5500, 5, "42", 0),
    (100, 999, 9, "99", 9)
]

for i, (start, finish, limit, s, expected) in enumerate(test_cases):
    result = sol.numberOfPowerfulInt(start, finish, limit, s)
    print(f"Test {i+1}: {result == expected}, Got {result}, Expected {expected}")