class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            rot_top = rot_bot = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float('inf')
                if t != x:
                    rot_top += 1
                if b != x:
                    rot_bot += 1
            return min(rot_top, rot_bot)

        ans = min(check(tops[0]), check(bottoms[0]))
        return -1 if ans == float('inf') else ans

if __name__ == "__main__":
    s = Solution()
    print(s.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2])) 
    print(s.minDominoRotations([3,5,1,2,3], [3,6,3,3,4])) 