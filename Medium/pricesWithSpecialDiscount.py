class Solution:
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        result = prices[:]  
        
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break  
        
        return result
    
prices = [8, 4, 6, 2, 3]
solution = Solution()
print(solution.finalPrices(prices))  # Output: [4, 2, 4, 2, 3]
