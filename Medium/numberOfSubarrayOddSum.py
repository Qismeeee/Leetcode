class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            if current_sum % 2 == 0:
                result += odd_count  
                even_count += 1
            else:
                result += even_count  
                odd_count += 1
            
            result %= MOD 
        return result


def test_numOfSubarrays():
    solution = Solution()

    # Test case 1: arr = [1, 3, 5]
    arr = [1, 3, 5]
    print(solution.numOfSubarrays(arr))  

    # Test case 2: arr = [2, 4, 6]
    arr = [2, 4, 6]
    print(solution.numOfSubarrays(arr))  

    # Test case 3: arr = [1, 2, 3, 4, 5, 6, 7]
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(solution.numOfSubarrays(arr))  

    # Test case 4: arr = [1]
    arr = [1]
    print(solution.numOfSubarrays(arr))  

    # Test case 5: arr = [2]
    arr = [2]
    print(solution.numOfSubarrays(arr))  

    # Test case 6: arr = [1, 2, 3]
    arr = [1, 2, 3]
    print(solution.numOfSubarrays(arr))  

test_numOfSubarrays()
