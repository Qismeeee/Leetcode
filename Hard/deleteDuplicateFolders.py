class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.deleted = False
        
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
        
        signature_to_nodes = defaultdict(list)
        
        def get_signature(node):
            if not node.children:
                return ""
            
            child_sigs = []
            for name, child in node.children.items():
                child_sig = get_signature(child)
                child_sigs.append((name, child_sig))
            
            child_sigs.sort()
            
            signature = ",".join("{}({})".format(name, sig) for name, sig in child_sigs)
            if signature:
                signature_to_nodes[signature].append(node)
            
            return signature
        
        get_signature(root)
        
        def mark_deleted(node):
            node.deleted = True
            for child in node.children.values():
                mark_deleted(child)
        
        for signature, nodes in signature_to_nodes.items():
            if len(nodes) > 1:  # Duplicate found
                for node in nodes:
                    mark_deleted(node)
        result = []
        
        def collect_paths(node, current_path):
            if node.deleted:
                return
            if current_path:
                result.append(current_path[:])
            
            for name, child in node.children.items():
                current_path.append(name)
                collect_paths(child, current_path)
                current_path.pop()
        
        collect_paths(root, [])
        return result
    

def test_solution():
    sol = Solution()
    paths1 = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
    print("Example 1:")
    print("Input:", paths1)
    print("Output:", sol.deleteDuplicateFolder(paths1))
    print()
    
    paths2 = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
    print("Example 2:")
    print("Input:", paths2)
    print("Output:", sol.deleteDuplicateFolder(paths2))
    print()
    
    paths3 = [["a","b"],["c","d"],["c"],["a"]]
    print("Example 3:")
    print("Input:", paths3)
    print("Output:", sol.deleteDuplicateFolder(paths3))
    print()

test_solution()