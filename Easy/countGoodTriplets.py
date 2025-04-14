class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0
        n = len(arr)
        for i in range(n - 2):  
            for j in range(i + 1, n - 1): 
                for k in range(j + 1, n): 
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count


solution = Solution()

# Test case 1
arr1 = [3, 0, 1, 1, 9, 7]
a1, b1, c1 = 7, 2, 3
print(solution.countGoodTriplets(arr1, a1, b1, c1))  

# Test case 2
arr2 = [1, 1, 2, 2, 3]
a2, b2, c2 = 0, 0, 1
print(solution.countGoodTriplets(arr2, a2, b2, c2))  

# Test case 3
arr3 = [5, 3, 6, 2, 4, 7]
a3, b3, c3 = 3, 2, 3
print(solution.countGoodTriplets(arr3, a3, b3, c3)) 

# Test case 4
arr4 = [10, 20, 30]
a4, b4, c4 = 5, 5, 5
print(solution.countGoodTriplets(arr4, a4, b4, c4))  

