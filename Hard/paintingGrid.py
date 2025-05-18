class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        from itertools import product
        from collections import defaultdict
        def is_valid(state):
            for i in range(1, len(state)):
                if state[i] == state[i-1]:
                    return False
            return True

        all_states = [s for s in product([0, 1, 2], repeat=m) if is_valid(s)]
        transitions = defaultdict(list)
        for a in all_states:
            for b in all_states:
                if all(x != y for x, y in zip(a, b)):
                    transitions[a].append(b)

        dp = defaultdict(int)
        for state in all_states:
            dp[state] = 1

        for _ in range(n - 1):
            new_dp = defaultdict(int)
            for prev in dp:
                for nxt in transitions[prev]:
                    new_dp[nxt] = (new_dp[nxt] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD

sol = Solution()
print(sol.colorTheGrid(1, 1))  
print(sol.colorTheGrid(1, 2))  
print(sol.colorTheGrid(5, 5))  