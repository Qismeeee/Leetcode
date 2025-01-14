class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        result = []
        setA = set()
        setB = set()
        
        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            common_elements = setA & setB
            result.append(len(common_elements))
        
        return result

def test_case(solution):
    # Test case 1
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    print(solution.findThePrefixCommonArray(A, B))  # Expected output: [0, 2, 3, 4]

    # Test case 2
    A = [2, 3, 1]
    B = [3, 1, 2]
    print(solution.findThePrefixCommonArray(A, B))  # Expected output: [0, 1, 3]

    # Test case 3 - All elements are common at every step
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]
    print(solution.findThePrefixCommonArray(A, B))  # Expected output: [1, 2, 3, 4]

    # Test case 4 - No common elements at all
    A = [1, 2, 3, 4]
    B = [5, 6, 7, 8]
    print(solution.findThePrefixCommonArray(A, B))  # Expected output: [0, 0, 0, 0]

    # Test case 5 - Only first element is common
    A = [1, 2, 3, 4]
    B = [1, 5, 6, 7]
    print(solution.findThePrefixCommonArray(A, B))  # Expected output: [1, 1, 1, 1]

solution = Solution()
test_case(solution)
