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
    
def run_tests():
    s = Solution()
    cases = [
        (9, 3, 13),
        (15, 4, 19),
        (1, 2, 1),
        (2, 2, 3),
        (5, 5, 6),
        (100, 3, 149),
    ]
    for b, e, expected in cases:
        out = s.numWaterBottles(b, e)
        assert out == expected, f"{b},{e}: expected {expected}, got {out}"
        print((b, e), out)

run_tests()