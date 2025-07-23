class Solution(object):
    def maximumGain(self, s, x, y):
        if x >= y:
            return self.removeAndGain(s, "ab", x, "ba", y)
        else:
            return self.removeAndGain(s, "ba", y, "ab", x)
    
    def removeAndGain(self, s, first_pattern, first_points, second_pattern, second_points):
        total_points = 0
        
        stack = []
        for char in s:
            if (stack and 
                stack[-1] == first_pattern[0] and 
                char == first_pattern[1]):
                stack.pop()
                total_points += first_points
            else:
                stack.append(char)
        
        remaining = stack
        stack = []
        for char in remaining:
            if (stack and 
                stack[-1] == second_pattern[0] and 
                char == second_pattern[1]):
                stack.pop()
                total_points += second_points
            else:
                stack.append(char)
        
        return total_points
    
sol = Solution()
print(sol.maximumGain("cdbcbbaaabab", 4, 5))
print(sol.maximumGain("aabbaaxybbaabb", 5, 4))
print(sol.maximumGain("ab", 1, 1))
print(sol.maximumGain("ba", 1, 1))