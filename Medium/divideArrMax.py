class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            triplet = nums[i:i+3]
            if triplet[-1] - triplet[0] > k:
                return []
            res.append(triplet)
        return res
    
if __name__ == "__main__":
    tests = [
        ([1,3,4,8,7,9,3,5,1], 2, [[1,1,3],[3,4,5],[7,8,9]]),
        ([2,4,2,2,5,2], 2, []),
        ([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14, None),
        ([1,2,3,4,5,6], 5, [[1,2,3],[4,5,6]]),
        ([1,10,2,9,3,8], 1, [])
    ]
    for nums, k, expected in tests:
        result = Solution().divideArray(nums[:], k)
        ok = (result == expected) if expected is not None else "ANY" if result else "FAIL"
        print(f"nums={nums}, k={k} -> {result} expected={expected} => {ok}")