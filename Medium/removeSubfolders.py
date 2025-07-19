class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        
        result = []
        for path in folder:
            if not result or not path.startswith(result[-1] + '/'):
                result.append(path)
        
        return result

def test_solution():
    sol = Solution()
    
    folder1 = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    print("Input:", folder1)
    print("Output:", sol.removeSubfolders(folder1))
    print()
    
    folder2 = ["/a","/a/b/c","/a/b/d"]
    print("Input:", folder2)
    print("Output:", sol.removeSubfolders(folder2))
    print()
    
    folder3 = ["/a/b/c","/a/b/ca","/a/b/d"]
    print("Input:", folder3)
    print("Output:", sol.removeSubfolders(folder3))

test_solution()