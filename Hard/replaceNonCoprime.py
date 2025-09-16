class Solution(object):
    def replaceNonCoprimes(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        st = []
        for x in nums:
            cur = x
            while st:
                g = gcd(st[-1], cur)
                if g == 1:
                    break
                cur = (st[-1] // g) * cur
                st.pop()
            st.append(cur)
        return st

def run_tests():
    s = Solution()
    cases = [
        ([6,4,3,2,7,6,2], [12,7,6]),
        ([2,2,1,1,3,3,3], [2,1,1,3]),
        ([1], [1]),
        ([2,3,5,7], [2,3,5,7]),
        ([4,8,3], [8,3]),
        ([2,6,8], [24]),
        ([45,15,5], [45]),
        ([10,20,5], [20]),
    ]
    for nums, expected in cases:
        out = s.replaceNonCoprimes(nums)
        assert out == expected, f"{nums}: expected {expected}, got {out}"
        print(nums, "->", out)

run_tests()
