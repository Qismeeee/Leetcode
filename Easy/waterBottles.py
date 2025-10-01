class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = 0
        full = numBottles
        empty = 0
        while full > 0:
            total += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
        return total