class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        from collections import Counter
        
        freq = Counter(s)
        valid_chars = []
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if freq[char] >= k:
                valid_chars.append(char)
        
        def can_repeat_k_times(seq):
            """Check if seq can be repeated k times as subsequence of s"""
            if not seq:
                return True
                
            target = seq * k
            i = 0 
            
            for char in target:
                while i < len(s) and s[i] != char:
                    i += 1
                if i == len(s):
                    return False
                i += 1  
            return True
        current_level = [""]
        
        while True:
            next_level = set()  
            for seq in current_level:
                for char in valid_chars:
                    new_seq = seq + char
                    
                    if can_repeat_k_times(new_seq):
                        next_level.add(new_seq)
            
            if not next_level:
                break
            
            current_level = list(next_level)
        return max(current_level) if current_level else ""
        

def test_solution():
    sol = Solution()
    
    result1 = sol.longestSubsequenceRepeatedK("letsleetcode", 2)
    print(f"Example 1: '{result1}'")  
    result2 = sol.longestSubsequenceRepeatedK("bb", 2)
    print(f"Example 2: '{result2}'")  
    result3 = sol.longestSubsequenceRepeatedK("ab", 2)
    print(f"Example 3: '{result3}'")  
    s = "letsleetcode"
    k = 2
    print(f"\nTracing Example 1: s='{s}', k={k}")
    
    from collections import Counter
    freq = Counter(s)
    print(f"Character frequencies: {dict(freq)}")
    
    valid_chars = [char for char in 'abcdefghijklmnopqrstuvwxyz' if freq[char] >= k]
    print(f"Valid characters (freq >= {k}): {valid_chars}")
    
    target = "let" * 2  
    print(f"Checking if '{target}' is subsequence of '{s}':")
    i = 0
    for char in target:
        while i < len(s) and s[i] != char:
            i += 1
        if i < len(s):
            print(f"  Found '{char}' at position {i}")
            i += 1
        else:
            print(f"  Could not find '{char}'")
            break
    
    print(f"\nAdditional tests:")
    print(f"longestSubsequenceRepeatedK('aabb', 2): '{sol.longestSubsequenceRepeatedK('aabb', 2)}'")
    print(f"longestSubsequenceRepeatedK('aaabbbccc', 3): '{sol.longestSubsequenceRepeatedK('aaabbbccc', 3)}'")

test_solution()