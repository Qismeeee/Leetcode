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
