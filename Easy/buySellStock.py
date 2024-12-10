class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > max_profit:
                max_profit = price - buy
        return max_profit

solution = Solution()
prices = [7,6,4,3,1]
max_profit = solution.maxProfit(prices)
print(max_profit)       


prices = [7,1,5,3,6,4]
max_profit = solution.maxProfit(prices)
print(max_profit)   