class Solution(object):
   def maximumCandies(self, candies, k):
       """
       :type candies: List[int]
       :type k: int
       :rtype: int
       """
       if sum(candies) < k:
           return 0
       
       left, right = 1, max(candies)
       
       while left <= right:
           mid = (left + right) // 2
           children_count = sum(pile // mid for pile in candies)
           
           if children_count >= k:
               left = mid + 1
           else:
               right = mid - 1
               
       return right

# Test cases
test_cases = [
   ([5, 8, 6], 3),  
   ([2, 5], 11),     
   ([4, 7, 5], 4),     
   ([10], 1),         
   ([1, 2, 3, 4, 5], 5) 
]

for candies, k in test_cases:
   result = Solution().maximumCandies(candies, k)
   print(f"candies = {candies}, k = {k}, result = {result}")