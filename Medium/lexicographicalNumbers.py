class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur % 10 != 9 and cur + 1 <= n:
                    cur += 1
                else:
                    while cur % 10 == 9 or cur + 1 > n:
                        cur //= 10
                    cur += 1
        return res
