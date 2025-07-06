class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        
        # Create frequency map for nums2 values
        self.freq = {}
        for num in nums2:
            self.freq[num] = self.freq.get(num, 0) + 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        
        # Update frequency map: remove old value, add new value
        self.freq[old_val] -= 1
        if self.freq[old_val] == 0:
            del self.freq[old_val]
        
        self.freq[new_val] = self.freq.get(new_val, 0) + 1
        self.nums2[index] = new_val

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        result = 0
        for num1 in self.nums1:
            target = tot - num1
            if target in self.freq:
                result += self.freq[target]
        return result

findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(findSumPairs.count(7))
findSumPairs.add(3, 2)
print(findSumPairs.count(8))
print(findSumPairs.count(4))
findSumPairs.add(0, 1)
findSumPairs.add(1, 1)
print(findSumPairs.count(7))