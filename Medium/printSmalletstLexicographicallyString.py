class Solution(object):
    def robotWithString(self, s):
        min_char = [None] * len(s)
        min_c = 'z'
        for i in range(len(s) - 1, -1, -1):
            min_c = min(min_c, s[i])
            min_char[i] = min_c
        
        t = []
        result = []
        
        for i, c in enumerate(s):
            t.append(c)
            while t and (i == len(s) - 1 or t[-1] <= min_char[i + 1]):
                result.append(t.pop())
        
        return ''.join(result)

solution = Solution()

print(solution.robotWithString("zza"))  
print(solution.robotWithString("bac")) 
print(solution.robotWithString("bdda")) 
print(solution.robotWithString("cba"))
print(solution.robotWithString("abc")) 
