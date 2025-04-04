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

def test():
    sol = Solution()
    
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    print(sol.lcaDeepestLeaves(root1).val)  

    root2 = TreeNode(1)
    print(sol.lcaDeepestLeaves(root2).val) 

    root3 = TreeNode(0)
    root3.left = TreeNode(1)
    root3.right = TreeNode(3)
    root3.left.right = TreeNode(2)
    print(sol.lcaDeepestLeaves(root3).val)

test()
