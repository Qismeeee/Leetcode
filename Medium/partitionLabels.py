class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        result = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                result.append(end - start + 1)  
                start = i + 1  
        return result
    
solution = Solution()
test_cases = [
    "ababcbacadefegdehijhklij",  
    "eccbbbbdec",                
    "abcdefg",                   
    "aaa",                      
    "aaabbc",                  
]

for test in test_cases:
    result = solution.partitionLabels(test)
    print(f"Input: s = \"{test}\"")
    print(f"Output: {result}")
    print("-----")