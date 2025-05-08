import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**30
        dist = [[[INF]*2 for _ in range(m)] for __ in range(n)]
        dist[0][0][0] = 0
        hq = [(0, 0, 0, 0)]  # time, i, j, parity (0→ next cost=1, 1→ next cost=2)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while hq:
            t, i, j, p = heapq.heappop(hq)
            if t > dist[i][j][p]: continue
            if i==n-1 and j==m-1:
                return t
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    start = max(t, moveTime[ni][nj])
                    cost = 1 if p==0 else 2
                    nt = start + cost
                    np = 1-p
                    if nt < dist[ni][nj][np]:
                        dist[ni][nj][np] = nt
                        heapq.heappush(hq, (nt, ni, nj, np))
        return -1
