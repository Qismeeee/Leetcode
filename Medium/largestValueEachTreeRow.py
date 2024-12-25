from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            max_value = float('-inf')
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_value)
        
        return result
    

def test_largest_values():
    def build_tree(nodes):
        if not nodes:
            return None
        from collections import deque
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root
    
    test_cases = [
        ([1, 3, 2, 5, 3, None, 9], [1, 3, 9]), 
        ([1, 2, 3], [1, 3]), 
        ([1], [1]),  # Single node tree
        ([], []),  # Empty tree
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),  # Skewed tree
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7]),  # Perfect binary tree
    ]
    
    solution = Solution()
    for i, (input_tree, expected) in enumerate(test_cases):
        root = build_tree(input_tree)
        output = solution.largestValues(root)
        print(f"Test case {i + 1}: {'Passed' if output == expected else 'Failed'}")
        print(f"Expected: {expected}, Got: {output}")

test_largest_values()
