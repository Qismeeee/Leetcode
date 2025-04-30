class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(1 for n in nums if len(str(n)) % 2 == 0)


if __name__ == "__main__":
    s = Solution()
    print(s.countSubarrays([2, 1, 4, 3, 5], 10))  
    print(s.countSubarrays([1, 1, 1], 5))  