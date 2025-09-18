import heapq

class TaskManager(object):

    def __init__(self, tasks):
        self.info = {}  # taskId -> (userId, priority)
        self.heap = []  # (-priority, -taskId, taskId)
        for userId, taskId, priority in tasks:
            self.info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        self.info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        userId, _ = self.info[taskId]
        self.info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.info:
            del self.info[taskId]

    def execTop(self):
        while self.heap:
            neg_p, neg_tid, tid = self.heap[0]
            if tid not in self.info:
                heapq.heappop(self.heap)
                continue
            uid, p = self.info[tid]
            if -neg_p != p:
                heapq.heappop(self.heap)
                continue
            heapq.heappop(self.heap)
            del self.info[tid]
            return uid
        return -1
