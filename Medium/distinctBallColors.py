class Solution(object):
    def queryResults(self, limit, queries):
        c=0
        added_colors={}
        balls = {}
        ret = []
        for q in queries:
            if q[0] in balls:
                added_colors[balls[q[0]]]-=1
                if not added_colors[balls[q[0]]]:
                    c-=1
            if added_colors.get(q[1], 0):
                added_colors[q[1]]+=1
            else:
                added_colors[q[1]]=1
                c+=1
            balls[q[0]]=q[1]
            ret.append(c)
        return ret

def test_query_results():
    sol = Solution()

    # Test Case 1
    limit = 4
    queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
    expected_output = [1, 2, 2, 3]
    assert sol.queryResults(limit, queries) == expected_output
    print("Test Case 1 Passed")

    # Test Case 2
    limit = 4
    queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
    expected_output = [1, 2, 2, 3, 4]
    assert sol.queryResults(limit, queries) == expected_output
    print("Test Case 2 Passed")

    # Test Case 3 (All balls get the same color)
    limit = 3
    queries = [[0, 1], [1, 1], [2, 1], [3, 1]]
    expected_output = [1, 1, 1, 1]
    assert sol.queryResults(limit, queries) == expected_output
    print("Test Case 3 Passed")

    # Test Case 4 (Changing colors frequently)
    limit = 5
    queries = [[0, 2], [1, 3], [2, 4], [0, 5], [1, 6]]
    expected_output = [1, 2, 3, 3, 3]
    assert sol.queryResults(limit, queries) == expected_output
    print("Test Case 4 Passed")

    # Test Case 5 (Only one ball gets different colors)
    limit = 1
    queries = [[0, 1], [0, 2], [0, 3], [0, 4]]
    expected_output = [1, 1, 1, 1]
    assert sol.queryResults(limit, queries) == expected_output
    print("Test Case 5 Passed")

    print("All Test Cases Passed!")

# Run tests
test_query_results()
