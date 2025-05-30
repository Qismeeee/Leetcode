class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n

        d = 0
        curr = node1
        while curr != -1 and dist1[curr] == -1:
            dist1[curr] = d
            d += 1
            curr = edges[curr]

        d = 0
        curr = node2
        while curr != -1 and dist2[curr] == -1:
            dist2[curr] = d
            d += 1
            curr = edges[curr]

        answer = -1
        best = float('inf')
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                m = max(dist1[i], dist2[i])
                if m < best or (m == best and i < answer):
                    best = m
                    answer = i
        return answer
