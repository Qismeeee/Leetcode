class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        s, e, t = startTime, endTime, eventTime
        q = [s[0] - 0]
        for i in range(1, len(s)):
            q.append(s[i] - e[i - 1])
        q.append(t - e[-1])

        max_free = total = sum(q[:k + 1])
        for i in range(k + 1, len(q)):
            total += q[i] - q[i - k - 1]
            if total > max_free:
                max_free = total

        return max_free


def test_solution():
    sol = Solution()
    
    test_cases = [
        {
            "eventTime": 5,
            "k": 1,
            "startTime": [1,3],
            "endTime": [2,5],
            "expected": 2,
            "description": "Basic example 1"
        },
        {
            "eventTime": 10,
            "k": 1,
            "startTime": [0,2,9],
            "endTime": [1,4,10],
            "expected": 6,
            "description": "Basic example 2"
        },
        {
            "eventTime": 5,
            "k": 2,
            "startTime": [0,1,2,3,4],
            "endTime": [1,2,3,4,5],
            "expected": 0,
            "description": "No free time available"
        },
        {
            "eventTime": 10,
            "k": 0,
            "startTime": [2,5,8],
            "endTime": [3,6,9],
            "expected": 2,
            "description": "No moves allowed"
        },
        {
            "eventTime": 20,
            "k": 1,
            "startTime": [2,5,8,12,15],
            "endTime": [3,6,9,13,16],
            "expected": 6,
            "description": "Multiple small gaps"
        },
        {
            "eventTime": 100,
            "k": 2,
            "startTime": [10,20,30,40],
            "endTime": [15,25,35,45],
            "expected": 65,
            "description": "Large gaps available"
        },
        {
            "eventTime": 15,
            "k": 3,
            "startTime": [1,3,5,7,9],
            "endTime": [2,4,6,8,10],
            "expected": 11,
            "description": "Can remove many meetings"
        },
        {
            "eventTime": 8,
            "k": 1,
            "startTime": [0,2,4,6],
            "endTime": [1,3,5,7],
            "expected": 2,
            "description": "Regular spacing"
        },
        {
            "eventTime": 12,
            "k": 2,
            "startTime": [1,4,7,10],
            "endTime": [2,5,8,11],
            "expected": 7,
            "description": "Combine multiple gaps"
        },
        {
            "eventTime": 6,
            "k": 1,
            "startTime": [1,2,3,4],
            "endTime": [2,3,4,5],
            "expected": 2,
            "description": "Adjacent meetings"
        },
        {
            "eventTime": 50,
            "k": 0,
            "startTime": [5,15,25,35],
            "endTime": [10,20,30,40],
            "expected": 10,
            "description": "Find largest existing gap"
        },
        {
            "eventTime": 30,
            "k": 5,
            "startTime": [2,4,6,8,10,12],
            "endTime": [3,5,7,9,11,13],
            "expected": 19,
            "description": "Remove most meetings"
        },
        {
            "eventTime": 7,
            "k": 1,
            "startTime": [0,6],
            "endTime": [1,7],
            "expected": 6,
            "description": "Two meetings far apart"
        },
        {
            "eventTime": 4,
            "k": 1,
            "startTime": [0,1,2,3],
            "endTime": [1,2,3,4],
            "expected": 1,
            "description": "No gaps originally"
        },
        {
            "eventTime": 25,
            "k": 2,
            "startTime": [3,8,13,18],
            "endTime": [5,10,15,20],
            "expected": 12,
            "description": "Medium complexity case"
        }
    ]
    
    print("Running test cases for Max Free Time solution")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases):
        eventTime = test["eventTime"]
        k = test["k"]
        startTime = test["startTime"]
        endTime = test["endTime"]
        expected = test["expected"]
        description = test["description"]
        
        result = sol.maxFreeTime(eventTime, k, startTime, endTime)
        
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        
        print(f"Test {i+1}: {description}")
        print(f"  Input: eventTime={eventTime}, k={k}")
        print(f"  Meetings: {list(zip(startTime, endTime))}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        
        if status == "FAIL":
            s, e, t = startTime, endTime, eventTime
            q = [s[0] - 0]
            for j in range(1, len(s)):
                q.append(s[j] - e[j - 1])
            q.append(t - e[-1])
            print(f"  Debug - Gaps: {q}")
            print(f"  Debug - Window size: {k+1}")
            
            max_sum = sum(q[:k+1])
            best_window = f"q[0:{k+1}] = {q[:k+1]}"
            for start in range(1, len(q) - k):
                window_sum = sum(q[start:start+k+1])
                if window_sum > max_sum:
                    max_sum = window_sum
                    best_window = f"q[{start}:{start+k+1}] = {q[start:start+k+1]}"
            print(f"  Debug - Best window: {best_window} = {max_sum}")
        
        print()
    
    print(f"Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! ✓")
    else:
        print(f"{total - passed} tests failed! ✗")

if __name__ == "__main__":
    test_solution()