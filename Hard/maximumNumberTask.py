import bisect

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1)//2
            usedPills = 0
            avail = workers[-mid:]            
            canAssign = True

            for t in reversed(tasks[:mid]):
                if avail[-1] >= t:
                    avail.pop()
                else:
                    idx = bisect.bisect_left(avail, t - strength)
                    if idx == len(avail) or usedPills == pills:
                        canAssign = False
                        break
                    usedPills += 1
                    avail.pop(idx)

            if canAssign:
                left = mid
            else:
                right = mid - 1

        return left
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxTaskAssign([3,2,1], [0,3,3], 1, 1))
    print(s.maxTaskAssign([5,4], [0,0,0], 1, 5))
    print(s.maxTaskAssign([10,15,30], [0,10,10,10,10], 3, 10))