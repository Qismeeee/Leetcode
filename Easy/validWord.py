class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False
        
        for char in word:
            if not char.isalnum():
                return False
            if char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        
        return has_vowel and has_consonant
    

def test_solution():
    sol = Solution()
    
    result1 = sol.isValid("234Adas")
    print(f"Example 1: '{result1}'")  
    result2 = sol.isValid("b3")
    print(f"Example 2: '{result2}'")  
    result3 = sol.isValid("a3$e")
    print(f"Example 3: '{result3}'")  
    print(f"\nTracing examples:")
    
    word1 = "234Adas"
    print(f"\nExample 1: '{word1}'")
    print(f"  Length: {len(word1)} >= 3? {len(word1) >= 3}")
    print(f"  Characters: ", end="")
    for char in word1:
        print(f"'{char}'({char.isalnum()})", end=" ")
    print()
    
    vowels_found = [c for c in word1 if c.lower() in 'aeiou']
    consonants_found = [c for c in word1 if c.isalpha() and c.lower() not in 'aeiou']
    print(f"  Vowels found: {vowels_found}")
    print(f"  Consonants found: {consonants_found}")
    print(f"  Result: {sol.isValid(word1)}")
    
    word2 = "b3"
    print(f"\nExample 2: '{word2}'")
    print(f"  Length: {len(word2)} >= 3? {len(word2) >= 3}")
    vowels_found2 = [c for c in word2 if c.lower() in 'aeiou']
    consonants_found2 = [c for c in word2 if c.isalpha() and c.lower() not in 'aeiou']
    print(f"  Vowels found: {vowels_found2}")
    print(f"  Consonants found: {consonants_found2}")
    print(f"  Result: {sol.isValid(word2)}")
    
    word3 = "a3$e"
    print(f"\nExample 3: '{word3}'")
    print(f"  Length: {len(word3)} >= 3? {len(word3) >= 3}")
    print(f"  Invalid characters: ", end="")
    invalid_chars = [c for c in word3 if not c.isalnum()]
    print(invalid_chars if invalid_chars else "None")
    print(f"  Result: {sol.isValid(word3)}")
    
    print(f"\nAdditional tests:")
    test_cases = [
        "abc",     
        "123",      
        "aei",      
        "bcd",      
        "a1b",      
        "A1B2E3F",  
        "ab@c",     
        "ae",       
    ]
    
    for test in test_cases:
        result = sol.isValid(test)
        print(f"  '{test}' -> {result}")

test_solution()