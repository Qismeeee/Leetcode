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
