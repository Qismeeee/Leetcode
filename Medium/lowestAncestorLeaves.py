class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def dfs(node):
            if not node:
                return (None, 0)  
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)
            if left_depth == right_depth:
                return (node, left_depth + 1)
            elif left_depth > right_depth:
                return (left_lca, left_depth + 1)
            else:
                return (right_lca, right_depth + 1)
        lca, _ = dfs(root)
        return lca
