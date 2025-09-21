import heapq
from collections import defaultdict

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        self.price = {}                         # (shop, movie) -> price
        self.movie_heap = defaultdict(list)     # movie -> [(price, shop, avail_gen)]
        self.rented_heap = []                   # [(price, shop, movie, rent_gen)]

        self.available = {}                     # (shop, movie) -> bool
        self.avail_gen = defaultdict(int)       # (shop, movie) -> int
        self.rented = {}                        # (shop, movie) -> bool
        self.rent_gen = defaultdict(int)        # (shop, movie) -> int

        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            self.available[(shop, movie)] = True
            self.rented[(shop, movie)] = False
            self.avail_gen[(shop, movie)] = 1
            self.rent_gen[(shop, movie)] = 0
            heapq.heappush(self.movie_heap[movie], (p, shop, 1))

    def _clean_movie_heap(self, movie):
        h = self.movie_heap[movie]
        while h:
            p, s, g = h[0]
            if not self.available.get((s, movie), False) or self.avail_gen[(s, movie)] != g:
                heapq.heappop(h)
            else:
                break

    def _clean_rented_heap(self):
        h = self.rented_heap
        while h:
            p, s, m, g = h[0]
            if not self.rented.get((s, m), False) or self.rent_gen[(s, m)] != g:
                heapq.heappop(h)
            else:
                break

    def search(self, movie):
        self._clean_movie_heap(movie)
        h = self.movie_heap[movie]
        res = []
        popped = []

        while h and len(res) < 5:
            p, s, g = heapq.heappop(h)
            if self.available.get((s, movie), False) and self.avail_gen[(s, movie)] == g:
                res.append(s)
                popped.append((p, s, g))

        for item in popped:
            heapq.heappush(h, item)
        return res

    def rent(self, shop, movie):
        key = (shop, movie)
        if self.available.get(key, False):
            self.available[key] = False
        self.rented[key] = True
        self.rent_gen[key] += 1
        heapq.heappush(self.rented_heap, (self.price[key], shop, movie, self.rent_gen[key]))

    def drop(self, shop, movie):
        key = (shop, movie)
        if self.rented.get(key, False):
            self.rented[key] = False
            self.available[key] = True
            self.avail_gen[key] += 1
            heapq.heappush(self.movie_heap[movie], (self.price[key], shop, self.avail_gen[key]))

    def report(self):
        self._clean_rented_heap()
        h = self.rented_heap
        res = []
        popped = []

        while h and len(res) < 5:
            p, s, m, g = heapq.heappop(h)
            if self.rented.get((s, m), False) and self.rent_gen[(s, m)] == g:
                res.append([s, m])
                popped.append((p, s, m, g))

        for item in popped:
            heapq.heappush(h, item)
        return res
    
def run_tests():
    m = MovieRentingSystem(3, [[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]])
    assert m.search(1) == [1,0,2]
    m.rent(0,1)
    m.rent(1,2)
    assert m.report() == [[0,1],[1,2]]
    m.drop(1,2)
    assert m.search(2) == [0,1]
    print("case1 ok")

    m = MovieRentingSystem(2, [[0,10,5],[1,10,5]])
    assert m.search(10) == [0,1]
    m.rent(1,10)
    assert m.search(10) == [0]
    assert m.report() == [[1,10]]
    m.drop(1,10)
    assert m.search(10) == [0,1]
    print("case2 ok")

    m = MovieRentingSystem(4, [[0,7,3],[1,7,3],[2,7,4],[3,7,3]])
    assert m.search(7) == [0,1,3,2]
    m.rent(0,7); m.rent(1,7); m.rent(3,7)
    assert m.report() == [[0,7],[1,7],[3,7]]
    m.drop(1,7)
    assert m.search(7) == [1,2]
    print("case3 ok")

    m = MovieRentingSystem(5, [[0,1,8],[1,2,5],[2,3,5],[3,4,5],[4,5,6],[0,2,5]])
    assert m.search(2) == [0,1]
    m.rent(1,2); m.rent(2,3); m.rent(3,4); m.rent(0,2)
    r = m.report()
    assert r == [[1,2],[2,3],[3,4],[0,2]]
    m.drop(0,2)
    assert m.search(2) == [0]
    print("case4 ok")

run_tests()

