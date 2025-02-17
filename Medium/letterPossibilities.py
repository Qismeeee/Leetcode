class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        result = set()
        def backtrack(path, remaining_tiles):
            if path:
                result.add(path) 
            for i in range(len(remaining_tiles)):
                if i > 0 and remaining_tiles[i] == remaining_tiles[i - 1]:
                    continue
                backtrack(path + remaining_tiles[i], remaining_tiles[:i] + remaining_tiles[i + 1:])
        
        tiles = sorted(tiles)
        backtrack("", tiles)
        return len(result)

# Test case 1: Input: "AAB"
tiles = "AAB"
solution = Solution()
print(solution.numTilePossibilities(tiles)) 

# Test case 2: Input: "AAABBC"
tiles = "AAABBC"
solution = Solution()
print(solution.numTilePossibilities(tiles))  

# Test case 3: Input: "V"
tiles = "V"
solution = Solution()
print(solution.numTilePossibilities(tiles))  

# Test case 4: Input: "ABC"
tiles = "ABC"
solution = Solution()
print(solution.numTilePossibilities(tiles))  
