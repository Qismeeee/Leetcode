from collections import defaultdict

class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        pos_by_val = defaultdict(list)
        for i, v in enumerate(nums):
            if v > 0:
                pos_by_val[v].append(i)

        if not pos_by_val:
            return 0

        # DSU over indices [0..n-1]
        parent = list(range(n))
        rank = [0] * n
        active = [False] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b, cur_tag):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            hasA = (root_tag[ra] == cur_tag)
            hasB = (root_tag[rb] == cur_tag)
            # union by rank
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
                hasA, hasB = hasB, hasA
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            if hasA or hasB:
                root_tag[ra] = cur_tag
            # return info whether both had current value
            return hasA and hasB

        # root_tag[r] = "version" in which this root contains at least one
        # index with current value; compared to cur_tag
        root_tag = [-1] * n

        ans = 0
        # process values in decreasing order
        for cur_tag, val in enumerate(sorted(pos_by_val.keys(), reverse=True)):
            comp_v = 0  # number of components that contain at least one 'val'
            for idx in pos_by_val[val]:
                active[idx] = True
                parent[idx] = idx
                rank[idx] = 0
                root_tag[idx] = cur_tag
                comp_v += 1

            for idx in pos_by_val[val]:
                for nb in (idx - 1, idx + 1):
                    if 0 <= nb < n and active[nb]:
                        merged_two_v = union(idx, nb, cur_tag)
                        if merged_two_v:
                            comp_v -= 1

            ans += comp_v

        return ans


s = Solution()

print(s.minOperations([0,2]))           # 1
print(s.minOperations([3,1,2,1]))       # 3
print(s.minOperations([1,2,1,2,1,2]))   # 4
print(s.minOperations([0,0,0]))         # 0
