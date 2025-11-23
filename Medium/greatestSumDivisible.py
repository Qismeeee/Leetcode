class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        r = total % 3
        if r == 0:
            return total

        inf = 10**18
        min1 = [inf, inf]  # two smallest numbers with x % 3 == 1
        min2 = [inf, inf]  # two smallest numbers with x % 3 == 2

        for x in nums:
            if x % 3 == 1:
                if x < min1[0]:
                    min1[1] = min1[0]
                    min1[0] = x
                elif x < min1[1]:
                    min1[1] = x
            elif x % 3 == 2:
                if x < min2[0]:
                    min2[1] = min2[0]
                    min2[0] = x
                elif x < min2[1]:
                    min2[1] = x

        if r == 1:
            # remove either one %3==1 or two %3==2
            option1 = min1[0]
            option2 = min2[0] + min2[1]
        else:  # r == 2
            # remove either one %3==2 or two %3==1
            option1 = min2[0]
            option2 = min1[0] + min1[1]

        remove = min(option1, option2)
        if remove >= inf:
            return 0
        return total - remove


s = Solution()

print(s.maxSumDivThree([3,6,5,1,8]))     # 18
print(s.maxSumDivThree([4]))             # 0
print(s.maxSumDivThree([1,2,3,4,4]))     # 12
print(s.maxSumDivThree([1,1,1]))         # 3
print(s.maxSumDivThree([2,2,2,2]))       # 6
print(s.maxSumDivThree([7,11,14]))       # 0
