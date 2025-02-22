class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        stack = []
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)
            if stack:
                if depth > stack[-1][0]:
                    stack[-1][1].left = node
                else:
                    while stack and stack[-1][0] >= depth:
                        stack.pop()
                    stack[-1][1].right = node
            stack.append((depth, node))
        return stack[0][1]


sol = Solution()

# Test các test case
test_cases = [
    "1",
    "1-2--3---4",
    "1-2--3---4-5--6",
    "1-2--3---4-5--6---7",
    "1-401--349---90--88"
]

for case in test_cases:
    root = sol.recoverFromPreorder(case)
    def print_tree(node):
        if not node:
            return "null"
        return str(node.val) + "," + print_tree(node.left) + "," + print_tree(node.right)
    
    print(f"Input: {case}")
    print(f"Output: [{print_tree(root)}]\n")