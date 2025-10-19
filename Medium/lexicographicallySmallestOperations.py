from collections import deque

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        n = len(s)

        def add_op(x):
            arr = list(x)
            for i in range(1, n, 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            return ''.join(arr)

        def rot_op(x):
            return x[-b:] + x[:-b]

        seen = set([s])
        q = deque([s])
        best = s
        while q:
            cur = q.popleft()
            if cur < best:
                best = cur

            x = add_op(cur)
            if x not in seen:
                seen.add(x)
                q.append(x)

            y = rot_op(cur)
            if y not in seen:
                seen.add(y)
                q.append(y)

        return best

s = "5525"; a = 9; b = 2
sol = Solution()
print(sol.findLexSmallestString(s, a, b))

s = "74"; a = 5; b = 1
print(sol.findLexSmallestString(s, a, b))

s = "0011"; a = 4; b = 2
print(sol.findLexSmallestString(s, a, b))
