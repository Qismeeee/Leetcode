class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  
        
        n = len(nums)
        parent = list(range(n))  
        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= limit:
                    union(i, j)
        
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        result = nums[:]
        for group in groups.values():
            sorted_values = sorted(result[i] for i in group)
            for idx, value in zip(sorted(group), sorted_values):
                result[idx] = value
        
        return result

# Test Case 1:
nums1 = [1, 5, 3, 9, 8]
limit1 = 2
solution = Solution()
print(solution.lexicographicallySmallestArray(nums1, limit1))  # Expected Output: [1, 3, 5, 8, 9]

# Test Case 2:
nums2 = [1, 7, 6, 18, 2, 1]
limit2 = 3
print(solution.lexicographicallySmallestArray(nums2, limit2))  # Expected Output: [1, 6, 7, 18, 1, 2]

# Test Case 3:
nums3 = [1, 7, 28, 19, 10]
limit3 = 3
print(solution.lexicographicallySmallestArray(nums3, limit3))  # Expected Output: [1, 7, 28, 19, 10]

# Test Case 4:
nums4 = [10, 20, 30, 40]
limit4 = 15
print(solution.lexicographicallySmallestArray(nums4, limit4))  # Expected Output: [10, 20, 30, 40]

# Test Case 5:
nums5 = [5, 5, 5, 5, 5]
limit5 = 0
print(solution.lexicographicallySmallestArray(nums5, limit5))  # Expected Output: [5, 5, 5, 5, 5]

# Test Case 6:
nums6 = [9, 1, 5, 7, 3]
limit6 = 5
print(solution.lexicographicallySmallestArray(nums6, limit6))  # Expected Output: [1, 5, 7, 9, 3]
