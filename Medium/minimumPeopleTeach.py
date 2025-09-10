class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        L = [set(x) for x in languages]
        need = set()
        for u, v in friendships:
            if L[u-1].isdisjoint(L[v-1]):
                need.add(u-1)
                need.add(v-1)
        if not need:
            return 0
        cnt = [0]*(n+1)
        for u in need:
            for lang in L[u]:
                cnt[lang] += 1
        return len(need) - max(cnt)

def run_tests():
    s = Solution()
    cases = [
        (2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]], 1),
        (3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]], 2),
        (3, [[1,2],[2],[2,3]], [[1,2],[2,3]], 0),
        (3, [[1],[2],[3]], [[1,2],[2,3],[1,3]], 2),
        (2, [[1],[1],[1]], [[1,2],[2,3]], 0),
    ]
    for n, languages, friendships, expected in cases:
        res = s.minimumTeachings(n, languages, friendships)
        assert res == expected, f"expected {expected}, got {res}"
        print((n, languages, friendships), res)

run_tests()
