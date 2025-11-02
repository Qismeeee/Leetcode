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
