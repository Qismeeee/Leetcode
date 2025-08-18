class Solution(object):
    def judgePoint24(self, cards):
        nums = [float(x) for x in cards]
        EPS = 1e-6

        def dfs(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPS

            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = arr[i], arr[j]
                    rest = [arr[k] for k in range(n) if k != i and k != j]

                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for c in candidates:
                        if dfs(rest + [c]):
                            return True
            return False

        return dfs(nums)

def run_tests():
    sol = Solution()
    cases = [
        ([4,1,8,7], True),
        ([1,2,1,2], False),
        ([2,2,3,3], True),
        ([1,3,4,6], True),
        ([1,1,1,1], False),
        ([6,6,6,6], True),
        ([3,3,8,8], True),
        ([5,5,5,1], True),
        ([1,2,3,4], True),
        ([9,9,9,9], False),
    ]
    for cards, expected in cases:
        got = sol.judgePoint24(cards)
        assert got == expected, (cards, expected, got)
    print("OK")

run_tests()
