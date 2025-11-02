class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        G = set(map(tuple, guards))
        W = set(map(tuple, walls))
        B = G | W
        guarded = set()
        for r in range(m):
            seen = False
            for c in range(n):
                p = (r, c)
                if p in W: seen = False
                elif p in G: seen = True
                elif seen: guarded.add(p)
            seen = False
            for c in range(n - 1, -1, -1):
                p = (r, c)
                if p in W: seen = False
                elif p in G: seen = True
                elif seen: guarded.add(p)
        for c in range(n):
            seen = False
            for r in range(m):
                p = (r, c)
                if p in W: seen = False
                elif p in G: seen = True
                elif seen: guarded.add(p)
            seen = False
            for r in range(m - 1, -1, -1):
                p = (r, c)
                if p in W: seen = False
                elif p in G: seen = True
                elif seen: guarded.add(p)
        total_empty = m * n - len(B)
        return total_empty - len(guarded)


m = 4; n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
s = Solution()
print(s.countUnguarded(m, n, guards, walls))  # 7

m = 3; n = 3
guards = [[1,1]]
walls = [[0,1],[1,0],[2,1],[1,2]]
print(s.countUnguarded(m, n, guards, walls))  # 4
