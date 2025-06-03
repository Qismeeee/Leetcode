from collections import deque

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        visited = set()
        haveKeys = set()
        waiting = set()
        dq = deque(initialBoxes)
        total = 0
        while dq:
            box = dq.popleft()
            if box in visited:
                continue
            if status[box] == 1 or box in haveKeys:
                visited.add(box)
                total += candies[box]
                for k in keys[box]:
                    if k not in haveKeys:
                        haveKeys.add(k)
                        if k in waiting:
                            dq.append(k)
                            waiting.remove(k)
                for cb in containedBoxes[box]:
                    dq.append(cb)
            else:
                waiting.add(box)
        return total

if __name__ == "__main__":
    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[1],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [0]
    print(Solution().maxCandies(status,candies,keys,containedBoxes,initialBoxes))

    status = [1,0,0,0,0,0]
    candies = [1,1,1,1,1,1]
    keys = [[1,2,3,4,5],[],[],[],[],[]]
    containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]
    initialBoxes = [0]
    print(Solution().maxCandies(status,candies,keys,containedBoxes,initialBoxes))
