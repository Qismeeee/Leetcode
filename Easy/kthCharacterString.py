
class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        if k == 1:
            return 'a'
        n = 0
        while (1 << n) < k:
            n += 1
        prev_length = 1 << (n - 1)
        
        if k <= prev_length:
            return self.kthCharacter(k)
        else:
            pos_in_original = k - prev_length
            original_char = self.kthCharacter(pos_in_original)
            next_char = chr((ord(original_char) - ord('a') + 1) % 26 + ord('a'))
            return next_char

def test_solution():
    sol = Solution()
    result1 = sol.kthCharacter(5)
    print(f"Example 1 (k=5): '{result1}'")  
    result2 = sol.kthCharacter(10)
    print(f"Example 2 (k=10): '{result2}'") 
    def simulate_operations(target_length):
        word = "a"
        operations = 0
        
        while len(word) < target_length:
            generated = ""
            for char in word:
                next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                generated += next_char
            word += generated
            operations += 1
            print(f"After operation {operations}: '{word}' (length: {len(word)})")
            
            if len(word) >= target_length:
                break
        
        return word
    
    print(f"\nSimulating operations up to length 16:")
    result_string = simulate_operations(16)
    
    print(f"\nVerification:")
    print(f"5th character: '{result_string[4]}' (expected 'b')")
    print(f"10th character: '{result_string[9]}' (expected 'c')")
    
    # Additional test cases
    print(f"\nAdditional tests:")
    for k in [1, 2, 3, 4, 6, 7, 8]:
        char = sol.kthCharacter(k)
        actual_char = result_string[k-1] if k <= len(result_string) else "?"
        print(f"k={k}: got '{char}', actual '{actual_char}'")

test_solution()