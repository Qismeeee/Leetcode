class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] += 1
            
            while all(count[char] > 0 for char in 'abc'):
                count[s[left]] -= 1
                left += 1

            result += left
        return result


def test_cases():
    solution = Solution()
    
    # Test case 1
    s1 = "abcabc"
    print(f"Test case 1: s = {s1} => Output: {solution.numberOfSubstrings(s1)}")  
    
    # Test case 2
    s2 = "aaacb"
    print(f"Test case 2: s = {s2} => Output: {solution.numberOfSubstrings(s2)}")  
    
    # Test case 3
    s3 = "abc"
    print(f"Test case 3: s = {s3} => Output: {solution.numberOfSubstrings(s3)}") 
    
    # Test case 4 (edge case with minimum length)
    s4 = "aab"
    print(f"Test case 4: s = {s4} => Output: {solution.numberOfSubstrings(s4)}")  
    
    # Test case 5 (string with no 'c')
    s5 = "aaaabbb"
    print(f"Test case 5: s = {s5} => Output: {solution.numberOfSubstrings(s5)}")  

test_cases()