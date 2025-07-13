class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        
        i = j = 0  
        matches = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1
        return matches


def test_solution():
    sol = Solution()
    result1 = sol.matchPlayersAndTrainers([4,7,9], [8,2,5,8])
    print(f"Example 1: {result1}")  
    result2 = sol.matchPlayersAndTrainers([1,1,1], [10])
    print(f"Example 2: {result2}")  
    print(f"All match: {sol.matchPlayersAndTrainers([1,2,3], [4,5,6])}")  # 3
    print(f"None match: {sol.matchPlayersAndTrainers([5,6,7], [1,2,3])}")  # 0
    print(f"Partial: {sol.matchPlayersAndTrainers([1,2,3], [2,3])}")  # 2

test_solution()