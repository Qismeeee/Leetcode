# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        queue = [root]
        level = 0 

        while queue:
            size = len(queue)
            current_level = []

            for _ in range(size):
                node = queue.pop(0)
                current_level.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                values = [node.val for node in current_level][::-1]
                for i, node in enumerate(current_level):
                    node.val = values[i]

            level += 1

        return root

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def level_order_traversal(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


values = [2, 3, 5, 8, 13, 21, 34]
root = build_tree(values)
solution = Solution()
reversed_root = solution.reverseOddLevels(root)
print(level_order_traversal(reversed_root)) 