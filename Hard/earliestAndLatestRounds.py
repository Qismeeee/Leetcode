class Solution(object):
    def earliestAndLatest(self, n, a, b):
        def simplify(n, a, b):
            if a>b: a, b = b, a
            if a+b >= n+1:
                a, b = n+1-b, n+1-a
            return n, a, b
    
        def get_info(n,a,b):
            ll, rr = a-1, n-b
            aa = n-ll
            bb = 1+rr
            return ll,rr,aa,bb

        def while_loop(n, a, b):
            ans = 1
            while a+b < n+1:
                n = (n+1)/2
                ans += 1
            if b-a-1==0:
                while n%2:
                    n = (n+1)/2
                    ans += 1
            return ans

        def solve_fast(n, a, b):
            n, a, b = simplify(n, a, b)
            if a+b == n+1: 
                return 1

            if b <= (n+1)/2:
                return while_loop(n, a, b)
            
            ll, rr, aa, bb = get_info(n, a, b)
            if (ll%2==1 and bb-a-1==0):
                if (n%2==0) and (b == n/2+1):                    
                    return 1 + while_loop((n+1)/2, a, a+1)
                else:
                    return 3
            else:
                return 2

        def solve_slow(n, a, b):
            n, a, b = simplify(n, a, b)
            if a+b==n+1: 
                return 1
            if b <= n+1-b:  
                return 1+solve_slow((n+1)/2, 1, 2)
            else:
                ll, rr, aa, bb = get_info(n, a, b)
                keep = (b-bb-1)/2 + n%2
                return 1+solve_slow((n+1)/2, 1, 1+keep+1) 

        return [solve_fast(n,a,b), solve_slow(n,a,b)]

def test_solution():
    sol = Solution()
    
    test_cases = [
        {
            "n": 11,
            "a": 2,
            "b": 4,
            "expected": [3, 4],
            "description": "Basic example 1"
        },
        {
            "n": 5,
            "a": 1,
            "b": 5,
            "expected": [1, 1],
            "description": "Direct competitors"
        },
        {
            "n": 3,
            "a": 1,
            "b": 3,
            "expected": [1, 1],
            "description": "Small tournament direct"
        },
        {
            "n": 4,
            "a": 1,
            "b": 2,
            "expected": [2, 2],
            "description": "Adjacent players"
        },
        {
            "n": 4,
            "a": 1,
            "b": 4,
            "expected": [1, 1],
            "description": "Opposite ends even"
        },
        {
            "n": 6,
            "a": 2,
            "b": 5,
            "expected": [2, 3],
            "description": "Medium tournament"
        },
        {
            "n": 8,
            "a": 1,
            "b": 8,
            "expected": [1, 1],
            "description": "Large direct competitors"
        },
        {
            "n": 8,
            "a": 2,
            "b": 7,
            "expected": [2, 3],
            "description": "Large near opposite"
        },
        {
            "n": 7,
            "a": 3,
            "b": 5,
            "expected": [2, 3],
            "description": "Odd tournament middle"
        },
        {
            "n": 10,
            "a": 3,
            "b": 8,
            "expected": [2, 3],
            "description": "Large asymmetric"
        },
        {
            "n": 12,
            "a": 4,
            "b": 9,
            "expected": [2, 3],
            "description": "Large even tournament"
        },
        {
            "n": 15,
            "a": 5,
            "b": 11,
            "expected": [2, 4],
            "description": "Large odd tournament"
        },
        {
            "n": 16,
            "a": 1,
            "b": 16,
            "expected": [1, 1],
            "description": "Power of 2 direct"
        },
        {
            "n": 16,
            "a": 7,
            "b": 10,
            "expected": [2, 4],
            "description": "Power of 2 complex"
        },
        {
            "n": 20,
            "a": 8,
            "b": 13,
            "expected": [2, 4],
            "description": "Large tournament case"
        },
        {
            "n": 9,
            "a": 2,
            "b": 8,
            "expected": [2, 3],
            "description": "Odd large tournament"
        },
        {
            "n": 14,
            "a": 6,
            "b": 9,
            "expected": [2, 3],
            "description": "Even medium tournament"
        },
        {
            "n": 13,
            "a": 4,
            "b": 10,
            "expected": [2, 3],
            "description": "Odd medium tournament"
        },
        {
            "n": 18,
            "a": 7,
            "b": 12,
            "expected": [2, 4],
            "description": "Large even case"
        },
        {
            "n": 21,
            "a": 9,
            "b": 13,
            "expected": [2, 4],
            "description": "Large odd case"
        }
    ]
    
    print("Testing Optimized Tournament Solution")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases):
        n = test["n"]
        a = test["a"]
        b = test["b"]
        expected = test["expected"]
        description = test["description"]
        
        result = sol.earliestAndLatest(n, a, b)
        
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        
        print(f"Test {i+1}: {description}")
        print(f"  Input: n={n}, a={a}, b={b}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        
        if status == "FAIL":
            simplified = (n, a, b) if a <= b else (n, b, a)
            if simplified[1] + simplified[2] >= n + 1:
                simplified = (n, n + 1 - simplified[2], n + 1 - simplified[1])
            
            print(f"  Debug - After simplify: n={simplified[0]}, a={simplified[1]}, b={simplified[2]}")
            print(f"  Debug - Direct competition check: {simplified[1]} + {simplified[2]} == {simplified[0]} + 1? {simplified[1] + simplified[2] == simplified[0] + 1}")
            
            if simplified[2] <= (simplified[0] + 1) / 2:
                print(f"  Debug - Case: b is on left/center")
            else:
                print(f"  Debug - Case: b is on right")
        
        print()
    
    print(f"Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! ✓")
    else:
        print(f"{total - passed} tests failed! ✗")

def edge_case_tests():
    sol = Solution()
    
    print("\nEdge case analysis:")
    print("=" * 30)
    
    edge_cases = [
        (2, 1, 2),
        (3, 1, 2),
        (3, 2, 3), 
        (4, 1, 3),
        (4, 2, 3),
        (4, 2, 4),
        (5, 2, 4),
        (6, 1, 6),
        (6, 3, 4),
        (7, 1, 7),
        (8, 3, 6),
        (9, 4, 6),
        (10, 1, 10)
    ]
    
    for n, a, b in edge_cases:
        result = sol.earliestAndLatest(n, a, b)
        print(f"n={n:2d}, a={a:2d}, b={b:2d} -> {result}")

if __name__ == "__main__":
    test_solution()
    edge_case_tests()