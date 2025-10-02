class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        totalDrunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            full = 1
            empty -= numExchange  
            totalDrunk += full    
            empty += full         
            numExchange += 1      
        return totalDrunk


s = Solution()
print(s.maxBottlesDrunk(13, 6)) 
print(s.maxBottlesDrunk(10, 3))  
print(s.maxBottlesDrunk(1, 2))   
print(s.maxBottlesDrunk(15, 4))