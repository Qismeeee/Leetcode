class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[0 for _ in range(k)] for _ in range(k)]
        ans = 0

        for num in nums:
            r = num % k
            for j in range(k):
                dp[r][j] = dp[j][r] + 1
                ans = max(ans, dp[r][j])

        return ans
    
def test_solution():
    sol = Solution()
    
    test_cases = [
        {
            "nums": [1,2,3,4,5],
            "k": 2,
            "expected": 5,
            "description": "Basic example - alternating odd/even"
        },
        {
            "nums": [1,4,2,3,1,4],
            "k": 3,
            "expected": 4,
            "description": "Basic example - alternating pattern"
        },
        {
            "nums": [2,4,6,8],
            "k": 3,
            "expected": 4,
            "description": "All same remainder"
        },
        {
            "nums": [1,3,5,7,9],
            "k": 2,
            "expected": 5,
            "description": "All odd numbers"
        },
        {
            "nums": [1,2],
            "k": 5,
            "expected": 2,
            "description": "Minimum length"
        },
        {
            "nums": [1,1,1,1],
            "k": 3,
            "expected": 4,
            "description": "All identical numbers"
        },
        {
            "nums": [1,2,3,1,2,3],
            "k": 4,
            "expected": 6,
            "description": "Perfect alternating cycle"
        },
        {
            "nums": [5,10,15,20,25],
            "k": 5,
            "expected": 5,
            "description": "All multiples of 5"
        },
        {
            "nums": [1,3,5,2,4,6],
            "k": 2,
            "expected": 6,
            "description": "Mixed order alternating pattern"
        },
        {
            "nums": [7,14,21,28,35],
            "k": 7,
            "expected": 5,
            "description": "All same remainder zero"
        },
        {
            "nums": [1,2,3,4,5,6,7,8,9,10],
            "k": 3,
            "expected": 4,
            "description": "Long sequence with k=3"
        },
        {
            "nums": [2,4,6,1,3,5],
            "k": 2,
            "expected": 6,
            "description": "Two groups same remainder"
        },
        {
            "nums": [10,20,30,11,21,31],
            "k": 10,
            "expected": 6,
            "description": "Alternating mod 10 pattern"
        },
        {
            "nums": [1,4,7,2,5,8,3,6,9],
            "k": 3,
            "expected": 3,
            "description": "Each remainder appears equally"
        },
        {
            "nums": [100,200,300,400],
            "k": 100,
            "expected": 4,
            "description": "Large numbers same remainder"
        },
        {
            "nums": [1,5,9,13,17],
            "k": 4,
            "expected": 5,
            "description": "Arithmetic progression mod 4"
        },
        {
            "nums": [2,7,3,8,4,9],
            "k": 5,
            "expected": 6,
            "description": "Alternating mod 5 pattern"
        },
        {
            "nums": [6,12,18,7,13,19],
            "k": 6,
            "expected": 6,
            "description": "Two remainder classes"
        },
        {
            "nums": [1,8,3,10,5,12],
            "k": 7,
            "expected": 6,
            "description": "Alternating pattern mod 7"
        },
        {
            "nums": [15,25,35,45,55],
            "k": 10,
            "expected": 5,
            "description": "All remainder 5 mod 10"
        }
    ]
    
    print("Testing DP Solution for Longest Valid Subsequence")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases):
        nums = test["nums"]
        k = test["k"]
        expected = test["expected"]
        description = test["description"]
        
        result = sol.maximumLength(nums, k)
        
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        
        print(f"Test {i+1}: {description}")
        print(f"  Input: nums={nums}, k={k}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        
        if status == "FAIL":
            remainders = [x % k for x in nums]
            print(f"  Debug - Remainders: {remainders}")
            
            from collections import Counter
            remainder_count = Counter(remainders)
            print(f"  Debug - Remainder counts: {dict(remainder_count)}")
            
            max_single = max(remainder_count.values()) if remainder_count else 0
            print(f"  Debug - Max single remainder count: {max_single}")
        
        print()
    
    print(f"Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed!")
    else:
        print(f"{total - passed} tests failed!")

def edge_case_tests():
    sol = Solution()
    
    print("\nEdge Case Testing")
    print("=" * 30)
    
    edge_cases = [
        ([1, 2], 1),
        ([1, 2], 10),
        ([1000000, 2000000], 1000),
        ([1, 1000], 999),
        ([3, 6, 9, 12], 3),
        ([1, 3, 5, 7, 9, 11], 2),
        ([2, 4, 8, 16], 4),
        ([1, 2, 3, 4, 5, 6], 6),
        ([7, 14, 21], 7),
        ([11, 22, 33, 44], 11)
    ]
    
    for nums, k in edge_cases:
        result = sol.maximumLength(nums, k)
        remainders = [x % k for x in nums]
        print(f"nums={nums}, k={k} -> {result}, remainders={remainders}")

def performance_test():
    sol = Solution()
    
    print("\nPerformance Test")
    print("=" * 20)
    
    import time
    
    large_nums = list(range(1, 1001))
    large_k = 100
    
    start_time = time.time()
    result = sol.maximumLength(large_nums, large_k)
    end_time = time.time()
    
    print(f"Large test: nums=1..1000, k={large_k}")
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    test_solution()
    edge_case_tests()
    performance_test()