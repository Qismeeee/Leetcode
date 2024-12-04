class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        result = 0
        for i in range(len(s) - 1):
            current_val = roman_map[s[i]]
            next_val = roman_map[s[i+1]]
            if current_val < next_val:
                result = result - current_val
            else:
                result = result + current_val

        result += roman_map[s[-1]]
        return result



s = Solution()
value = s.romanToInt("MCMXCIV")
print(value)
