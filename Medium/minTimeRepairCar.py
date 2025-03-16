class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def can_repair_all_in_time(time):
            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int((time // rank) ** 0.5)
                if total_cars_repaired >= cars:  
                    return True
            return total_cars_repaired >= cars
        
        low, high = 1, ranks[0] * cars * cars
        while low < high:
            mid = (low + high) // 2
            if can_repair_all_in_time(mid):
                high = mid 
            else:
                low = mid + 1  

        return low
    

ranks = [4, 2, 3, 1]
cars = 10

solution = Solution()
print(solution.repairCars(ranks, cars))

ranks = [5, 1, 8]
cars = 6

solution = Solution()
print(solution.repairCars(ranks, cars))

ranks = [10, 20, 30]
cars = 3

solution = Solution()
print(solution.repairCars(ranks, cars))

ranks = [1, 1, 1]
cars = 1

solution = Solution()
print(solution.repairCars(ranks, cars)) 
