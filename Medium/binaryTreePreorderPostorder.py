class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(pre_left, pre_right, post_left, post_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            if pre_left == pre_right:
                return root
            
            left_subtree_root_val = preorder[pre_left + 1]
            left_subtree_root_index_in_postorder = postorder_index_map[left_subtree_root_val]
            left_subtree_size = left_subtree_root_index_in_postorder - post_left + 1
            
            root.left = helper(pre_left + 1, pre_left + left_subtree_size, post_left, left_subtree_root_index_in_postorder)
            root.right = helper(pre_left + left_subtree_size + 1, pre_right, left_subtree_root_index_in_postorder + 1, post_right - 1)
            
            return root
        
        postorder_index_map = {value: idx for idx, value in enumerate(postorder)}
        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)