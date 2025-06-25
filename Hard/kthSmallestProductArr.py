import bisect, math

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        We will take a value mid using binary search and 
        try to see how many nums[i]*nums[j] values are lesser or equal to mid
        if we get count>=k , we will look to the left part of binary search
        else if count<=0 , we will look to the right part
        """
        def Check(mid):
            n = len(nums1)
            m = len(nums2)

            count = 0
            for n in nums1:
                if n > 0:
                    count += bisect.bisect_right(nums2,mid//n)
                elif n == 0:
                    count += m if mid>=0 else 0
                else:       
                    v = mid//n
                    if mid%n!=0:v+=1
                    count += (m - bisect.bisect_left(nums2,v))
          
            return count>=k
        
    
        l = -10**10
        r = 10**10

        while l<r:
            mid = l + (r-l)//2

            if Check(mid):
                r = mid
            else:
                l = mid+1
        
        return r

def generate_all_products(nums1, nums2):
    """Helper function to generate all products and sort them for verification"""
    products = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            products.append(nums1[i] * nums2[j])
    return sorted(products)

def test_solution():
    sol = Solution()
    
    test_cases = [
        # Basic test cases from examples
        {
            "nums1": [2,5], 
            "nums2": [3,4], 
            "k": 2,
            "expected": 8,
            "description": "Basic positive numbers"
        },
        {
            "nums1": [-4,-2,0,3], 
            "nums2": [2,4], 
            "k": 6,
            "expected": 0,
            "description": "Mixed with zero"
        },
        {
            "nums1": [-2,-1,0,1,2], 
            "nums2": [-3,-1,2,4,5], 
            "k": 3,
            "expected": -6,
            "description": "Mixed positive/negative"
        },
        
        # Edge cases
        {
            "nums1": [1], 
            "nums2": [1], 
            "k": 1,
            "expected": 1,
            "description": "Single elements"
        },
        {
            "nums1": [-1], 
            "nums2": [-1], 
            "k": 1,
            "expected": 1,
            "description": "Single negative elements"
        },
        {
            "nums1": [0], 
            "nums2": [1,2,3], 
            "k": 2,
            "expected": 0,
            "description": "Zero in nums1"
        },
        {
            "nums1": [1,2,3], 
            "nums2": [0], 
            "k": 1,
            "expected": 0,
            "description": "Zero in nums2"
        },
        
        # All negative
        {
            "nums1": [-3,-2,-1], 
            "nums2": [-3,-2,-1], 
            "k": 5,
            "expected": 4,
            "description": "All negative numbers"
        },
        
        # Large k
        {
            "nums1": [1,2], 
            "nums2": [3,4], 
            "k": 4,
            "expected": 8,
            "description": "k = total products"
        },
        
        # Test with larger numbers
        {
            "nums1": [-100,-50,0,50,100], 
            "nums2": [-200,-100,100,200], 
            "k": 10,
            "expected": -5000,
            "description": "Larger numbers"
        },
        
        # Test with repeated values
        {
            "nums1": [1,1,2,2], 
            "nums2": [3,3,4,4], 
            "k": 8,
            "expected": 6,
            "description": "Repeated values"
        }
    ]
    
    print("Testing Kth Smallest Product Solution")
    print("=" * 50)
    
    for i, test in enumerate(test_cases):
        nums1 = test["nums1"]
        nums2 = test["nums2"]
        k = test["k"]
        expected = test["expected"]
        description = test["description"]
        
        # Get actual result
        result = sol.kthSmallestProduct(nums1, nums2, k)
        
        # Verify with brute force
        all_products = generate_all_products(nums1, nums2)
        actual_expected = all_products[k-1]  # k is 1-based
        
        # Check results
        passed = (result == expected) and (result == actual_expected)
        status = "PASS" if passed else "FAIL"
        
        print(f"Test {i+1}: {description}")
        print(f"  nums1: {nums1}")
        print(f"  nums2: {nums2}")
        print(f"  k: {k}")
        print(f"  All products: {all_products}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Brute force: {actual_expected}")
        print(f"  Status: {status}")
        
        if not passed:
            print(f"  ERROR: Expected {expected}, got {result}")
        
        print()
    
    # Performance test with larger arrays
    print("Performance test with larger arrays:")
    large_nums1 = list(range(-50, 51))  # -50 to 50
    large_nums2 = list(range(-30, 31))  # -30 to 30
    k = 1500
    
    print(f"nums1 size: {len(large_nums1)}, nums2 size: {len(large_nums2)}")
    print(f"Total products: {len(large_nums1) * len(large_nums2)}")
    print(f"Finding k={k}th smallest...")
    
    try:
        result = sol.kthSmallestProduct(large_nums1, large_nums2, k)
        print(f"Result: {result}")
        print("Performance test: PASS")
    except Exception as e:
        print(f"Performance test: FAIL - {e}")

if __name__ == "__main__":
    test_solution()