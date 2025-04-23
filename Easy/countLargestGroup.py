class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict

        groups = defaultdict(int)

        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            groups[digit_sum] += 1

        max_size = max(groups.values())
        return sum(1 for count in groups.values() if count == max_size)
