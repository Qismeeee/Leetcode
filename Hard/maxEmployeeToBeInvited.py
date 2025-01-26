import unittest

class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        indegree = [0] * n
        for i in favorite:
            indegree[i] += 1

        visited = [False] * n
        def find_cycle(cur, start, path):
            visited[cur] = True
            path.append(cur)
            nxt = favorite[cur]
            if nxt == start:
                return path
            if not visited[nxt]:
                return find_cycle(nxt, start, path)
            return []

        cycles = []
        for i in range(n):
            if not visited[i] and indegree[i] == 1:
                cycle = find_cycle(i, i, [])
                if cycle:
                    cycles.append(cycle)

        max_cycle_len = max(len(cycle) for cycle in cycles) if cycles else 0

        visited = [False] * n
        def find_chain_len(cur):
            visited[cur] = True
            nxt = favorite[cur]
            if indegree[nxt] != 1:
                return 1
            if not visited[nxt]:
                return 1 + find_chain_len(nxt)
            return 1

        max_chain_sum = 0
        for i in range(n):
            if not visited[i] and indegree[i] > 1:
                j = favorite[i]
                if favorite[j] == i:
                    max_chain_sum += find_chain_len(i) + find_chain_len(j)

        return max(max_cycle_len, max_chain_sum)

class TestMaximumInvitations(unittest.TestCase):

    def test_example_1(self):
        favorite = [2, 2, 1, 2]
        self.assertEqual(Solution().maximumInvitations(favorite), 3)

    def test_example_2(self):
        favorite = [1, 2, 0]
        self.assertEqual(Solution().maximumInvitations(favorite), 3)

    def test_example_3(self):
        favorite = [3, 0, 1, 4, 1]
        self.assertEqual(Solution().maximumInvitations(favorite), 4)

    def test_no_cycle_no_chain(self):
        favorite = [1, 0, 3, 2]
        self.assertEqual(Solution().maximumInvitations(favorite), 2)

    def test_single_cycle(self):
        favorite = [1, 2, 0]
        self.assertEqual(Solution().maximumInvitations(favorite), 3)

    def test_multiple_cycles(self):
        favorite = [1, 2, 0, 4, 5, 3]
        self.assertEqual(Solution().maximumInvitations(favorite), 3)

if __name__ == '__main__':
    unittest.main()