
class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        groups = []
        i = 0
        
        while i < len(word):
            char = word[i]
            count = 1
            while i + count < len(word) and word[i + count] == char:
                count += 1
            
            groups.append(count)
            i += count
        total = 1  
        for group_length in groups:
            if group_length > 1:
                total += group_length - 1
        
        return total
    
def test_solution():
    sol = Solution()
    result1 = sol.possibleStringCount("abbcccc")
    print(f"Example 1: {result1}")  
    result2 = sol.possibleStringCount("abcd")
    print(f"Example 2: {result2}")  
    result3 = sol.possibleStringCount("aaaa")
    print(f"Example 3: {result3}")  
    word = "abbcccc"
    print(f"\nTracing Example 1: word = '{word}'")
    groups = []
    i = 0
    while i < len(word):
        char = word[i]
        count = 1
        while i + count < len(word) and word[i + count] == char:
            count += 1
        groups.append(count)
        print(f"Group: '{char}' × {count}")
        i += count
    
    print(f"Groups: {groups}")
    total = 1  # original string
    print(f"Original string: 1 way")
    
    for i, group_length in enumerate(groups):
        if group_length > 1:
            reductions = group_length - 1
            total += reductions
            print(f"Group {i+1} (length {group_length}): {reductions} reduction possibilities")
    
    print(f"Total: {total}")
    
    print(f"\nPossible strings for '{word}':")
    print("1. abbcccc (original)")
    print("2. abcccc (reduce 'bb' to 'b')")  
    print("3. abbccc (reduce 'cccc' to 'ccc')")
    print("4. abbcc (reduce 'cccc' to 'cc')")
    print("5. abbc (reduce 'cccc' to 'c')")

test_solution()