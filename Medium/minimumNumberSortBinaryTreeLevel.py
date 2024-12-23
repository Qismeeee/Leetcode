# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def min_swaps_to_sort(arr):
            n = len(arr)
            sorted_arr = sorted((value, index) for index, value in enumerate(arr))
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or sorted_arr[i][1] == i:
                    continue

                cycle_size = 0
                node = i

                while not visited[node]:
                    visited[node] = True
                    node = sorted_arr[node][1]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total_swaps += min_swaps_to_sort(current_level)

        return total_swaps


root = TreeNode(1, 
                TreeNode(4, TreeNode(7), TreeNode(6)), 
                TreeNode(3, TreeNode(8, TreeNode(9)), TreeNode(5, TreeNode(10))))

solution = Solution()
print(solution.minimumOperations(root))