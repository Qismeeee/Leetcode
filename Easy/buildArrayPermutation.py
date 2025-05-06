class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
    
if __name__ == "__main__":
    s = Solution()
    print(s.buildArray([0,2,1,5,3,4]), "expected", [0,1,2,4,5,3])
    print(s.buildArray([5,0,1,2,3,4]), "expected", [4,5,0,1,2,3])