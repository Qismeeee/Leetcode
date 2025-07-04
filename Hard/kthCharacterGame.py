class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        if k == 1:
            return 'a'
        
        length = 1
        ops_needed = 0
        
        while length < k and ops_needed < len(operations):
            length *= 2
            ops_needed += 1
        
        if ops_needed == 0:
            return 'a'
        prev_length = length // 2
        
        if k <= prev_length:
            return self.kthCharacter(k, operations[:ops_needed-1])
        else:
            pos_in_second_half = k - prev_length            
            char_from_first_half = self.kthCharacter(pos_in_second_half, operations[:ops_needed-1])
            
            if operations[ops_needed-1] == 1:
                shifted_char = chr((ord(char_from_first_half) - ord('a') + 1) % 26 + ord('a'))
                return shifted_char
            else:
                return char_from_first_half


def test_solution():
    sol = Solution()
    
    result1 = sol.kthCharacter(5, [0,0,0])
    print(f"Example 1 (k=5, ops=[0,0,0]): '{result1}'")  
    result2 = sol.kthCharacter(10, [0,1,0,1])
    print(f"Example 2 (k=10, ops=[0,1,0,1]): '{result2}'") 
    print(f"\nTracing Example 2:")
    
    def simulate_operations(operations, max_length=20):
        word = "a"
        print(f"Initial: '{word}' (length: {len(word)})")
        
        for i, op in enumerate(operations):
            if op == 0:
                word = word + word
                print(f"Op {i+1} (type 0): '{word}' (length: {len(word)})")
            else:
                shifted = ""
                for char in word:
                    next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                    shifted += next_char
                word = word + shifted
                print(f"Op {i+1} (type 1): '{word}' (length: {len(word)})")
            
            if len(word) >= max_length:
                break
        
        return word
    
    result_string = simulate_operations([0,1,0,1])
    if len(result_string) >= 10:
        print(f"10th character in actual string: '{result_string[9]}'")
    
    print(f"\nAdditional tests:")
    print(f"k=1, ops=[0]: '{sol.kthCharacter(1, [0])}'")  
    print(f"k=2, ops=[1]: '{sol.kthCharacter(2, [1])}'")  
    print(f"k=3, ops=[1,0]: '{sol.kthCharacter(3, [1,0])}'")  

test_solution()