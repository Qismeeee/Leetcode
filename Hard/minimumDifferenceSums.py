import heapq
import math
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        min_heap = nums[(2 * n) :]
        heapq.heapify(min_heap)

        max_sum = [0] * (n + 2)
        max_sum[n + 1] = sum(min_heap)
        for i in range((2 * n) - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            val = heapq.heappop(min_heap)
            max_sum[i - n + 1] = max_sum[i - n + 2] - val + nums[i]

        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)

        min_sum = [0] * (n + 2)
        min_sum[0] = -sum(max_heap)
        for i in range(n, (2 * n)):
            heapq.heappush(max_heap, -nums[i])
            val = -heapq.heappop(max_heap)
            min_sum[i - n + 1] = min_sum[i - n] - val + nums[i]

        ans = math.inf
        for i in range(0, n + 1):
            ans = min((min_sum[i] - max_sum[i + 1]), ans)

        return ans

def test_solution():
    sol = Solution()
    
    test_cases = [
        {
            "nums": [3,1,2],
            "expected": -1,
            "description": "Basic example n=1"
        },
        {
            "nums": [7,9,5,8,1,3],
            "expected": 1,
            "description": "Basic example n=2"
        },
        {
            "nums": [3,1,2,4,5,6],
            "expected": -1,
            "description": "Simple case n=2"
        },
        {
            "nums": [1,2,3,4,5,6,7,8,9],
            "expected": -3,
            "description": "Sequential numbers n=3"
        },
        {
            "nums": [10,5,15,20,1,25],
            "expected": -5,
            "description": "Mixed values n=2"
        },
        {
            "nums": [1,1,1,1,1,1],
            "expected": 0,
            "description": "All same values n=2"
        },
        {
            "nums": [1,2,3,7,8,9],
            "expected": -6,
            "description": "Two groups n=2"
        },
        {
            "nums": [20,6,1,8,4,3,2,5,10,15,12,7],
            "expected": -6,
            "description": "Larger case n=4"
        },
        {
            "nums": [2,1,3,6,5,4],
            "expected": 0,
            "description": "Optimal split n=2"
        },
        {
            "nums": [100,1,1,200,1,1],
            "expected": -99,
            "description": "Extreme values n=2"
        },
        {
            "nums": [5,10,15,1,2,3],
            "expected": 9,
            "description": "Ascending then small n=2"
        },
        {
            "nums": [1,10,1,10,1,10],
            "expected": 0,
            "description": "Alternating pattern n=2"
        },
        {
            "nums": [6,4,2,8,10,12],
            "expected": -6,
            "description": "Mixed order n=2"
        },
        {
            "nums": [1,2,3,4,5,6,7,8,9,10,11,12],
            "expected": -6,
            "description": "Sequential large n=4"
        },
        {
            "nums": [50,25,75,10,90,5],
            "expected": 15,
            "description": "Large range n=2"
        },
        {
            "nums": [3,3,3,6,6,6],
            "expected": -3,
            "description": "Two distinct values n=2"
        },
        {
            "nums": [1,100,1,100,1,100],
            "expected": 0,
            "description": "Binary values n=2"
        },
        {
            "nums": [7,1,8,2,9,3],
            "expected": 5,
            "description": "Interleaved n=2"
        },
        {
            "nums": [15,5,25,35,45,55],
            "expected": -20,
            "description": "Arithmetic progression n=2"
        },
        {
            "nums": [1,1,2,2,3,3],
            "expected": -1,
            "description": "Paired values n=2"
        }
    ]
    
    print("Testing Heap-Based Minimum Difference Solution")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases):
        nums = test["nums"]
        expected = test["expected"]
        description = test["description"]
        
        result = sol.minimumDifference(nums)
        
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        
        print(f"Test {i+1}: {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        
        if status == "FAIL":
            n = len(nums) // 3
            left_part = nums[:n]
            middle_part = nums[n:2*n]
            right_part = nums[2*n:]
            print(f"  Debug - n={n}")
            print(f"  Debug - Left: {left_part}")
            print(f"  Debug - Middle: {middle_part}")
            print(f"  Debug - Right: {right_part}")
        
        print()
    
    print(f"Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed!")
    else:
        print(f"{total - passed} tests failed!")

def stress_test():
    sol = Solution()
    
    print("\nStress Testing")
    print("=" * 20)
    
    import random
    
    for test_num in range(5):
        n = random.randint(1, 4)
        nums = [random.randint(1, 100) for _ in range(3 * n)]
        
        try:
            result = sol.minimumDifference(nums)
            print(f"Stress test {test_num + 1}: n={n}, result={result}")
        except Exception as e:
            print(f"Stress test {test_num + 1}: ERROR - {e}")

def edge_case_test():
    sol = Solution()
    
    print("\nEdge Case Testing")
    print("=" * 20)
    
    edge_cases = [
        [1, 2, 3],
        [1000000, 1, 1000000],
        [1, 1000000, 1],
        [999999, 1000000, 1],
        [1, 1, 1000000],
        [500000, 500000, 1000000]
    ]
    
    for i, nums in enumerate(edge_cases):
        try:
            result = sol.minimumDifference(nums)
            print(f"Edge case {i+1}: {nums} -> {result}")
        except Exception as e:
            print(f"Edge case {i+1}: ERROR - {e}")

if __name__ == "__main__":
    test_solution()
    stress_test()
    edge_case_test()