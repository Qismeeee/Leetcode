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
    
def run_tests():
    fr = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    )
    assert fr.highestRated("korean") == "kimchi"
    assert fr.highestRated("japanese") == "ramen"
    fr.changeRating("sushi", 16)
    assert fr.highestRated("japanese") == "sushi"
    fr.changeRating("ramen", 16)
    assert fr.highestRated("japanese") == "ramen"
    print("case1 ok")

    fr = FoodRatings(["aa","ab"], ["x","x"], [5,5])
    assert fr.highestRated("x") == "aa"
    fr.changeRating("ab", 6)
    assert fr.highestRated("x") == "ab"
    fr.changeRating("ab", 5)
    assert fr.highestRated("x") == "aa"
    print("case2 ok")

    fr = FoodRatings(["taco","burrito","pho"], ["mex","mex","viet"], [7,9,8])
    assert fr.highestRated("mex") == "burrito"
    fr.changeRating("taco", 10)
    assert fr.highestRated("mex") == "taco"
    assert fr.highestRated("viet") == "pho"
    print("case3 ok")

run_tests()

