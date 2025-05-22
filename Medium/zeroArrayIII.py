import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)

        used_query = []   # min-heap
        available_query = []  # max-heap
        queries.sort(key=lambda x: x[0])
        query_pos = 0
        applied_count = 0

        for i in range(n):
            while query_pos < len(queries) and queries[query_pos][0] == i:
                heapq.heappush(available_query, -queries[query_pos][1])
                query_pos += 1
            nums[i] -= len(used_query)

            while nums[i] > 0 and available_query and -available_query[0] >= i:
                heapq.heappush(used_query, -heapq.heappop(available_query))
                nums[i] -= 1
                applied_count += 1

            if nums[i] > 0:
                return -1

            while used_query and used_query[0] == i:
                heapq.heappop(used_query)

        return len(queries) - applied_count
    
nums = [1, 1, 1]
queries = [[0, 1], [1, 2], [0, 2]]

sol = Solution()
result = sol.maxRemoval(nums, queries)
print("Output:", result)