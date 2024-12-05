class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        start_pieces = "".join(c for c in start if c != '_')
        target_pieces = "".join(c for c in target if c != '_')
        if start_pieces != target_pieces:
            return False

        start_idx = 0
        target_idx = 0
        n = len(start)

        while start_idx < n and target_idx < n:
            while start_idx < n and start[start_idx] == '_':
                start_idx += 1
            while target_idx < n and target[target_idx] == '_':
                target_idx += 1

            if start_idx == n and target_idx == n:
                break
            if start_idx == n or target_idx == n:
                return False
            if start[start_idx] != target[target_idx]:
                return False
            if start[start_idx] == 'L' and start_idx < target_idx:
                return False
            if start[start_idx] == 'R' and start_idx > target_idx:
                return False

            start_idx += 1
            target_idx += 1
        return True


start = "_L__R__R_"
target = "L______RR"
solution = Solution()
print(solution.canChange(start, target)) 


start = "R_L_"
target = "__LR"
solution = Solution()
print(solution.canChange(start, target)) 
