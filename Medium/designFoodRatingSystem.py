import heapq
from collections import defaultdict

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.food2cuisine = {}
        self.food2rating = {}
        self.cuisine2heap = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food2cuisine[f] = c
            self.food2rating[f] = r
            heapq.heappush(self.cuisine2heap[c], (-r, f))

    def changeRating(self, food, newRating):
        c = self.food2cuisine[food]
        self.food2rating[food] = newRating
        heapq.heappush(self.cuisine2heap[c], (-newRating, food))

    def highestRated(self, cuisine):
        h = self.cuisine2heap[cuisine]
        while h and -h[0][0] != self.food2rating[h[0][1]]:
            heapq.heappop(h)
        return h[0][1]
