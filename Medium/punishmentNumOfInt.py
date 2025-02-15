class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def can_partition(num_str, target):
            """
            This helper function checks if the string representation of the square number can
            be split into contiguous substrings that sum to `target`.
            """
            length = len(num_str)
            def generate_partitions(start, current_sum):
                if start == length:
                    return current_sum == target
                
                for end in range(start + 1, length + 1):
                    part = num_str[start:end]
                    if part[0] != '0' or len(part) == 1:
                        new_sum = current_sum + int(part)
                        if generate_partitions(end, new_sum):
                            return True
                return False
            return generate_partitions(0, 0)
        
        total_sum = 0
        for i in range(1, n + 1):
            square = i * i
            square_str = str(square)
            if can_partition(square_str, i):
                total_sum += square
        
        return total_sum


sol = Solution()
# Test Case 1
n1 = 1
print(f"Test case n = {n1}: Expected = 1, Output = {sol.punishmentNumber(n1)}")

# Test Case 2
n2 = 9
print(f"Test case n = {n2}: Expected = 82, Output = {sol.punishmentNumber(n2)}")

# Test Case 3
n3 = 2
print(f"Test case n = {n3}: Expected = 1, Output = {sol.punishmentNumber(n3)}")

# Test Case 4
n4 = 15
print(f"Test case n = {n4}: Expected = 246, Output = {sol.punishmentNumber(n4)}")
