import collections
import heapq

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = collections.defaultdict(list) 
        self.valid_indices = {}  

    def change(self, index, number):
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number != number:
                self.valid_indices[(old_number, index)] = False 
        
        self.index_to_number[index] = number
        heapq.heappush(self.number_to_indices[number], index)
        self.valid_indices[(number, index)] = True 

    def find(self, number):
        if number not in self.number_to_indices:
            return -1
        
        while self.number_to_indices[number]:
            min_index = self.number_to_indices[number][0]
            if self.valid_indices.get((number, min_index), False):
                return min_index
            heapq.heappop(self.number_to_indices[number])  
        
        return -1