class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        travel_days = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )

        return dp[last_day]
    

def test():
    solution = Solution()
    
    # Test case 1
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print("Test Case 1: Expected 11, Got", solution.mincostTickets(days, costs))

    # Test case 2
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print("Test Case 2: Expected 17, Got", solution.mincostTickets(days, costs))

    # Additional test case 3
    days = [1, 15, 25, 35]
    costs = [5, 9, 20]
    print("Test Case 3: Expected 14, Got", solution.mincostTickets(days, costs))

    # Additional test case 4
    days = [1, 2, 4, 5, 6, 29, 30, 31]
    costs = [3, 8, 25]
    print("Test Case 4: Expected 16, Got", solution.mincostTickets(days, costs))

    # Additional test case 5
    days = [1, 365]
    costs = [2, 7, 15]
    print("Test Case 5: Expected 4, Got", solution.mincostTickets(days, costs))

test()