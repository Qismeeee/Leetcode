class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        id_to_value = {}        
        for id, value in nums1:
            id_to_value[id] = id_to_value.get(id, 0) + value
        
        for id, value in nums2:
            id_to_value[id] = id_to_value.get(id, 0) + value        
        result = [[id, value] for id, value in sorted(id_to_value.items())]
        
        return result


solution = Solution()
# Test Case 1: Simple case, some common ids
print(solution.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))  

# Test Case 2: No common ids, all ids are unique
print(solution.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))  

# Test Case 3: One array has a single element and the other array has multiple
print(solution.mergeArrays([[1, 2]], [[1, 3], [2, 4]]))  

# Test Case 4: Both arrays are empty
print(solution.mergeArrays([], []))  

# Test Case 5: Only one id in each array
print(solution.mergeArrays([[1, 10]], [[2, 20]]))  

# Test Case 6: One array with a single id and the other with duplicate values for the same id
print(solution.mergeArrays([[1, 10]], [[1, 20], [1, 30]]))  