class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for pre in prerequisites:
            reachable[pre[0]][pre[1]] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result

# Test case 1
numCourses = 2
prerequisites = [[1, 0]]
queries = [[0, 1], [1, 0]]
solution = Solution()
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [False, True]

# Test case 2
numCourses = 2
prerequisites = []
queries = [[1, 0], [0, 1]]
solution = Solution()
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [False, False]

# Test case 3
numCourses = 3
prerequisites = [[1, 2], [1, 0], [2, 0]]
queries = [[1, 0], [1, 2]]
solution = Solution()
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [True, True]

# Test case 4: Testing with multiple prerequisites
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
queries = [[0, 3], [1, 3], [2, 0], [3, 1]]
solution = Solution()
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [True, True, False, False]
