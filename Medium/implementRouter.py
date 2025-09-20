from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router(object):

    def __init__(self, memoryLimit):
        self.limit = memoryLimit
        self.q = deque()  # FIFO of (source, destination, timestamp)
        self.live = set()  # set of triples to detect duplicates
        self.dest_ts = defaultdict(list)   # destination -> increasing timestamps list
        self.dest_removed = defaultdict(int)  # destination -> how many earliest have been removed

    def _evict_if_needed(self):
        while len(self.q) > self.limit:
            s, d, t = self.q.popleft()
            self.live.discard((s, d, t))
            self.dest_removed[d] += 1  # remove oldest ts for this destination

    def addPacket(self, source, destination, timestamp):
        key = (source, destination, timestamp)
        if key in self.live:
            return False
        self.live.add(key)
        self.q.append(key)
        self.dest_ts[destination].append(timestamp)
        self._evict_if_needed()
        return True

    def forwardPacket(self):
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.live.discard((s, d, t))
        self.dest_removed[d] += 1
        return [s, d, t]

    def getCount(self, destination, startTime, endTime):
        arr = self.dest_ts.get(destination, [])
        if not arr:
            return 0
        l = bisect_left(arr, startTime)
        r = bisect_right(arr, endTime)
        rem = self.dest_removed.get(destination, 0)
        removed_in_range = max(0, min(rem, r) - min(rem, l))
        return (r - l) - removed_in_range


def run_tests():
    r = Router(3)
    assert r.addPacket(1,4,90) is True
    assert r.addPacket(2,5,90) is True
    assert r.addPacket(1,4,90) is False
    assert r.addPacket(3,5,95) is True
    assert r.addPacket(4,5,105) is True
    assert r.forwardPacket() == [2,5,90]
    assert r.addPacket(5,2,110) is True
    assert r.getCount(5,100,110) == 1
    print("case1 ok")

    r = Router(2)
    assert r.addPacket(7,4,90) is True
    assert r.forwardPacket() == [7,4,90]
    assert r.forwardPacket() == []
    print("case2 ok")

    r = Router(2)
    assert r.addPacket(1,9,10) is True
    assert r.addPacket(2,9,20) is True
    assert r.getCount(9,0,100) == 2
    assert r.addPacket(3,9,30) is True
    assert r.getCount(9,0,100) == 2
    assert r.forwardPacket() == [2,9,20]
    assert r.getCount(9,0,25) == 0
    assert r.getCount(9,21,40) == 1
    print("case3 ok")

    r = Router(5)
    assert r.addPacket(1,1,5) is True
    assert r.addPacket(1,1,6) is True
    assert r.addPacket(2,1,7) is True
    assert r.addPacket(3,2,8) is True
    assert r.getCount(1,5,7) == 3
    assert r.forwardPacket() == [1,1,5]
    assert r.getCount(1,5,7) == 2
    assert r.addPacket(4,1,9) is True
    assert r.getCount(1,6,9) == 3
    print("case4 ok")

run_tests()
