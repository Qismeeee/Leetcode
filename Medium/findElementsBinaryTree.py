class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.recovered = set()
        self.recover(root, 0)
    
    def recover(self, node, value):
        if node is None:
            return
        
        node.val = value
        self.recovered.add(value)
        if node.left:
            self.recover(node.left, 2 * value + 1)
        if node.right:
            self.recover(node.right, 2 * value + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.recovered



root = TreeNode(-1, TreeNode(-1, TreeNode(-1)), TreeNode(-1))
find_elements = FindElements(root)
print(find_elements.find(0))  
print(find_elements.find(1))  
print(find_elements.find(3))  
print(find_elements.find(2)) 
print(find_elements.find(4))  


root = TreeNode(-1, TreeNode(-1), TreeNode(-1, TreeNode(-1), TreeNode(-1)))
find_elements = FindElements(root)
print(find_elements.find(0))  
print(find_elements.find(1))  
print(find_elements.find(2))  
print(find_elements.find(3))  
print(find_elements.find(4))  
print(find_elements.find(5)) 
