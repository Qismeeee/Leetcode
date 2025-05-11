class Solution(object):
    def threeConsecutiveOdds(self, arr):
        velunexorai = arr
        count = 0
        for x in velunexorai:
            if x % 2:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

print(Solution().threeConsecutiveOdds([2,6,4,1]))
print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
print(Solution().threeConsecutiveOdds([1,3,5]))
print(Solution().threeConsecutiveOdds([1,1,2,1,1,1]))