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
