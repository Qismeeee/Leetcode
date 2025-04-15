class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        pos_in_nums2 = {val: idx for idx, val in enumerate(nums2)}
        transformed = [pos_in_nums2[num] for num in nums1]
        
        class FenwickTree:
            def __init__(self, size):
                self.size = size
                self.tree = [0] * (self.size + 1)
            
            def update(self, index, delta=1):
                while index <= self.size:
                    self.tree[index] += delta
                    index += index & -index
            
            def query(self, index):
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= index & -index
                return res
        
        max_val = n
        fenwick = FenwickTree(max_val)
        left_counts = [0] * n
        for i in range(n):
            val = transformed[i] + 1 
            left_counts[i] = fenwick.query(val - 1)
            fenwick.update(val)
        
        fenwick = FenwickTree(max_val)
        right_counts = [0] * n
        for i in range(n-1, -1, -1):
            val = transformed[i] + 1
            right_counts[i] = fenwick.query(max_val) - fenwick.query(val)
            fenwick.update(val)
        
        total = 0
        for i in range(n):
            total += left_counts[i] * right_counts[i]
        return total
        

def run_tests():
    solution = Solution()

    # Test Case 1: Example from the problem statement
    nums1 = [2, 0, 1, 3]
    nums2 = [0, 1, 2, 3]
    print(f"Test Case 1: {solution.goodTriplets(nums1, nums2)}")  

    # Test Case 2: Another example
    nums1 = [4, 0, 1, 3, 2]
    nums2 = [4, 1, 0, 2, 3]
    print(f"Test Case 2: {solution.goodTriplets(nums1, nums2)}")  

    # Test Case 3: No common subsequences with length greater than 2
    nums1 = [0, 1, 2]
    nums2 = [2, 0, 1]
    print(f"Test Case 3: {solution.goodTriplets(nums1, nums2)}") 

    # Test Case 4: Only one triplet possible
    nums1 = [0, 1, 2]
    nums2 = [0, 2, 1]
    print(f"Test Case 4: {solution.goodTriplets(nums1, nums2)}")  

    # Test Case 5: Multiple common subsequences
    nums1 = [1, 0, 2, 3]
    nums2 = [0, 2, 1, 3]
    print(f"Test Case 5: {solution.goodTriplets(nums1, nums2)}")  

    # Test Case 6: Edge case with smallest input
    nums1 = [0, 1, 2]
    nums2 = [0, 1, 2]
    print(f"Test Case 6: {solution.goodTriplets(nums1, nums2)}")  

run_tests()