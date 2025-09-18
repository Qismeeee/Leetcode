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


def run_tests():
    tm = TaskManager([[1,101,10],[2,102,20],[3,103,15]])
    tm.add(4,104,5)
    tm.edit(102,8)
    assert tm.execTop() == 3
    tm.rmv(101)
    tm.add(5,105,15)
    assert tm.execTop() == 5
    print("case1 ok")

    tm = TaskManager([[1,10,5],[2,20,5],[3,30,5]])
    assert tm.execTop() == 3
    assert tm.execTop() == 2
    assert tm.execTop() == 1
    assert tm.execTop() == -1
    print("case2 ok")

    tm = TaskManager([[1,1,1],[2,2,2]])
    tm.edit(1,5)
    assert tm.execTop() == 1
    assert tm.execTop() == 2
    assert tm.execTop() == -1
    print("case3 ok")

    tm = TaskManager([[9,9,7],[8,8,9]])
    tm.rmv(8)
    assert tm.execTop() == 9
    assert tm.execTop() == -1
    print("case4 ok")

    tm = TaskManager([])
    tm.add(1,100,10)
    tm.add(2,101,10)
    tm.add(3,102,9)
    assert tm.execTop() == 2
    assert tm.execTop() == 1
    assert tm.execTop() == 3
    assert tm.execTop() == -1
    print("case5 ok")

run_tests()
