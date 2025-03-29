class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        mod = 10**9 + 7
        
        prime_scores = [self.get_prime_score(num) for num in nums]
        
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        
        right = [n-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = n-1 if not stack else stack[-1] - 1
            stack.append(i)
        
        contributions = []
        for i in range(n):
            total_subarrays = (i - left[i] + 1) * (right[i] - i + 1)
            contributions.append((nums[i], total_subarrays))
        
        contributions.sort(key=lambda x: -x[0])
        
        result = 1
        remaining = k
        
        for val, count in contributions:
            use_count = min(count, remaining)
            result = (result * pow(val, use_count, mod)) % mod
            remaining -= use_count
            if remaining == 0:
                break
        
        return result
    
    def get_prime_score(self, x):
        if x == 1:
            return 0
        
        score = 0
        d = 2
        while d * d <= x:
            if x % d == 0:
                score += 1
                while x % d == 0:
                    x //= d
            d += 1
        if x > 1:
            score += 1
        return score

def test_maximum_score():
    solution = Solution()
    
    nums1 = [3, 5, 2]
    k1 = 2
    result1 = solution.maximumScore(nums1, k1)
    print(f"Test case 1: {result1}")
    
    nums2 = [6, 2, 10]
    k2 = 2
    result2 = solution.maximumScore(nums2, k2)
    print(f"Test case 2: {result2}")
    
    nums3 = [8, 3, 9, 3, 8]
    k3 = 2
    result3 = solution.maximumScore(nums3, k3)
    print(f"Test case 3: {result3}")

test_maximum_score()