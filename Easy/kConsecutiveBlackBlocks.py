class Solution(object):
    def minimumRecolors(self, blocks, k):
        min_recolors = float('inf')
        
        for i in range(len(blocks) - k + 1):
            window = blocks[i:i+k]
            recolors_needed = window.count('W')
            min_recolors = min(min_recolors, recolors_needed)
        
        return min_recolors

blocks = "WBWBBBW"
k = 2
solution = Solution()
print(solution.minimumRecolors(blocks, k))  

blocks = "WBBWWBBWBW"
k = 7
solution = Solution()
print(solution.minimumRecolors(blocks, k))  


blocks = "BBBBBB"
k = 5
solution = Solution()
print(solution.minimumRecolors(blocks, k))  

blocks = "WWWWWW"
k = 3
solution = Solution()
print(solution.minimumRecolors(blocks, k))  

blocks = "BBBW"
k = 4
solution = Solution()
print(solution.minimumRecolors(blocks, k)) 
