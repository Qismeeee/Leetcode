class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        w = 1
        ans = 0
        n = len(colors)
        for i in range(1, n+k-2 + 1):
            if colors[i % n] != colors[(i - 1 + n) % n]:
                w += 1
            else:
                w = 1
            if w >= k:
                ans += 1
        return ans
    

def test_solution():
    solution = Solution()
    # Test case 1
    colors1 = [0, 1, 0, 1, 0]
    k1 = 3
    print("Test Case 1:")
    print(f"colors = {colors1}, k = {k1} => Number of alternating groups = {solution.numberOfAlternatingGroups(colors1, k1)}")
    
    # Test case 2
    colors2 = [0, 1, 0, 0, 1, 0, 1]
    k2 = 6
    print("Test Case 2:")
    print(f"colors = {colors2}, k = {k2} => Number of alternating groups = {solution.numberOfAlternatingGroups(colors2, k2)}")
    
    # Test case 3
    colors3 = [1, 1, 0, 1]
    k3 = 4
    print("Test Case 3:")
    print(f"colors = {colors3}, k = {k3} => Number of alternating groups = {solution.numberOfAlternatingGroups(colors3, k3)}")

test_solution()