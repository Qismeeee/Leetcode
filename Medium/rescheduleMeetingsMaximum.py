class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        n = len(startTime)
        
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]

        maxLeft = [0] * (n + 1)
        maxLeft[0] = gaps[0]
        for i in range(1, n + 1):
            maxLeft[i] = max(maxLeft[i - 1], gaps[i])

        maxRight = [0] * (n + 1)
        maxRight[n] = gaps[n]
        for i in range(n - 1, -1, -1):
            maxRight[i] = max(maxRight[i + 1], gaps[i])

        res = 0
        for i in range(n):
            duration = endTime[i] - startTime[i]
            gap_sum = gaps[i] + gaps[i + 1]

            bestGap = 0
            if i > 0:
                bestGap = max(bestGap, maxLeft[i - 1])
            if i + 2 <= n:
                bestGap = max(bestGap, maxRight[i + 2])

            if duration <= bestGap:
                res = max(res, gap_sum + duration)
            else:
                res = max(res, gap_sum)

        return res

def test_solution():
    sol = Solution()
    
    test_cases = [
        {
            "eventTime": 5,
            "startTime": [1,3],
            "endTime": [2,5],
            "expected": 2,
            "description": "Basic example 1"
        },
        {
            "eventTime": 10,
            "startTime": [0,7,9],
            "endTime": [1,8,10],
            "expected": 7,
            "description": "Basic example 2"
        },
        {
            "eventTime": 10,
            "startTime": [0,3,7,9],
            "endTime": [1,4,8,10],
            "expected": 6,
            "description": "Basic example 3"
        },
        {
            "eventTime": 5,
            "startTime": [0,1,2,3,4],
            "endTime": [1,2,3,4,5],
            "expected": 0,
            "description": "No free time possible"
        },
        {
            "eventTime": 10,
            "startTime": [2,5],
            "endTime": [3,6],
            "expected": 4,
            "description": "Two meetings with large gaps"
        },
        {
            "eventTime": 8,
            "startTime": [1,3,5],
            "endTime": [2,4,6],
            "expected": 3,
            "description": "Three meetings equal gaps"
        },
        {
            "eventTime": 15,
            "startTime": [2,8,12],
            "endTime": [4,9,13],
            "expected": 5,
            "description": "Move small meeting to large gap"
        },
        {
            "eventTime": 12,
            "startTime": [1,4,7,10],
            "endTime": [2,5,8,11],
            "expected": 3,
            "description": "Multiple small meetings"
        },
        {
            "eventTime": 20,
            "startTime": [3,15],
            "endTime": [8,18],
            "expected": 8,
            "description": "One large meeting one small"
        },
        {
            "eventTime": 6,
            "startTime": [0,2,4],
            "endTime": [1,3,5],
            "expected": 2,
            "description": "Regular spacing pattern"
        },
        {
            "eventTime": 25,
            "startTime": [5,10,20],
            "endTime": [8,12,22],
            "expected": 13,
            "description": "Large gap at end"
        },
        {
            "eventTime": 14,
            "startTime": [2,6,10],
            "endTime": [4,8,12],
            "expected": 4,
            "description": "Even distribution"
        },
        {
            "eventTime": 7,
            "startTime": [1,5],
            "endTime": [3,6],
            "expected": 3,
            "description": "Simple two meetings case"
        },
        {
            "eventTime": 30,
            "startTime": [5,15,25],
            "endTime": [10,20,28],
            "expected": 10,
            "description": "Large gaps available"
        },
        {
            "eventTime": 18,
            "startTime": [2,8,14],
            "endTime": [5,11,16],
            "expected": 5,
            "description": "Move meeting to merge gaps"
        }
    ]
    
    print("Testing Optimized Max Free Time Solution")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases):
        eventTime = test["eventTime"]
        startTime = test["startTime"]
        endTime = test["endTime"]
        expected = test["expected"]
        description = test["description"]
        
        result = sol.maxFreeTime(eventTime, startTime, endTime)
        
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        
        print(f"Test {i+1}: {description}")
        print(f"  Input: eventTime={eventTime}")
        print(f"  Meetings: {list(zip(startTime, endTime))}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        
        if status == "FAIL":
            n = len(startTime)
            gaps = [0] * (n + 1)
            gaps[0] = startTime[0]
            for j in range(1, n):
                gaps[j] = startTime[j] - endTime[j - 1]
            gaps[n] = eventTime - endTime[n - 1]
            
            maxLeft = [0] * (n + 1)
            maxLeft[0] = gaps[0]
            for j in range(1, n + 1):
                maxLeft[j] = max(maxLeft[j - 1], gaps[j])
                
            maxRight = [0] * (n + 1)
            maxRight[n] = gaps[n]
            for j in range(n - 1, -1, -1):
                maxRight[j] = max(maxRight[j + 1], gaps[j])
            
            print(f"  Debug - Gaps: {gaps}")
            print(f"  Debug - MaxLeft: {maxLeft}")
            print(f"  Debug - MaxRight: {maxRight}")
            
            for j in range(n):
                duration = endTime[j] - startTime[j]
                gap_sum = gaps[j] + gaps[j + 1]
                bestGap = 0
                if j > 0:
                    bestGap = max(bestGap, maxLeft[j - 1])
                if j + 2 <= n:
                    bestGap = max(bestGap, maxRight[j + 2])
                
                can_move = duration <= bestGap
                contribution = gap_sum + duration if can_move else gap_sum
                print(f"  Meeting {j}: duration={duration}, gap_sum={gap_sum}, bestGap={bestGap}, can_move={can_move}, contrib={contribution}")
        
        print()
    
    print(f"Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! ✓")
    else:
        print(f"{total - passed} tests failed! ✗")

def manual_verify():
    print("\nManual verification of algorithm logic:")
    print("=" * 40)
    
    sol = Solution()
    eventTime, startTime, endTime = 10, [0,3,7,9], [1,4,8,10]
    
    n = len(startTime)
    gaps = [startTime[0]]
    for i in range(1, n):
        gaps.append(startTime[i] - endTime[i-1])
    gaps.append(eventTime - endTime[-1])
    
    print(f"Meetings: {list(zip(startTime, endTime))}")
    print(f"Gaps: {gaps}")
    print(f"Try removing each meeting and see max possible gain:")
    
    for i in range(n):
        duration = endTime[i] - startTime[i]
        gap_sum = gaps[i] + gaps[i+1]
        print(f"Remove meeting {i} [{startTime[i]},{endTime[i]}]: duration={duration}, merge gaps {gaps[i]}+{gaps[i+1]}={gap_sum}")
        
        other_gaps = gaps[:i] + gaps[i+2:]
        max_other = max(other_gaps) if other_gaps else 0
        print(f"  Max gap elsewhere: {max_other}")
        print(f"  Can relocate? {duration <= max_other}")
        print(f"  Final contribution: {gap_sum + duration if duration <= max_other else gap_sum}")

if __name__ == "__main__":
    test_solution()
    manual_verify()