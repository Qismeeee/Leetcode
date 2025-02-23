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
    

def print_preorder(root):
    if root:
        print(root.val, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)

def test():
    solution = Solution()

    # Test Case 1: Cây có 1 nút
    preorder = [1]
    postorder = [1]
    root = solution.constructFromPrePost(preorder, postorder)
    print("Test Case 1: ", end="")
    print_preorder(root)
    print() 

    # Test Case 2: Cây có 2 nút
    preorder = [1, 2]
    postorder = [2, 1]
    root = solution.constructFromPrePost(preorder, postorder)
    print("Test Case 2: ", end="")
    print_preorder(root)
    print() 

    # Test Case 3: Cây có 3 nút với cây con bên trái
    preorder = [1, 2, 3]
    postorder = [3, 2, 1]
    root = solution.constructFromPrePost(preorder, postorder)
    print("Test Case 3: ", end="")
    print_preorder(root)
    print() 

    # Test Case 4: Cây có 3 nút với cây con bên phải
    preorder = [1, 2, 3]
    postorder = [2, 3, 1]
    root = solution.constructFromPrePost(preorder, postorder)
    print("Test Case 4: ", end="")
    print_preorder(root)
    print() 

    # Test Case 5: Cây có 4 nút
    preorder = [1, 2, 4, 3]
    postorder = [4, 2, 3, 1]
    root = solution.constructFromPrePost(preorder, postorder)
    print("Test Case 5: ", end="")
    print_preorder(root)
    print()  

    # Test Case 6: Cây có 5 nút
    preorder = [1, 2, 4, 5, 3]
    postorder = [4, 5, 2, 3, 1]
    root = solution.constructFromPrePost(preorder, postorder)
    print("Test Case 6: ", end="")
    print_preorder(root)
    print() 

test()