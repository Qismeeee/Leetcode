from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        count_map = defaultdict(int)
        good_pairs = 0
        
        for i in range(n):
            delta = i - nums[i]
            good_pairs += count_map[delta]
            count_map[delta] += 1
        
        total_pairs = (n * (n - 1)) // 2
        return total_pairs - good_pairs

def test():
    solution = Solution()
    
    # Test case 1: Ví dụ đã cho trong đề bài
    nums1 = [4, 1, 3, 3]
    print(solution.countBadPairs(nums1))  # Expected output: 5

    # Test case 2: Một mảng đã sắp xếp tăng dần, không có bad pairs
    nums2 = [1, 2, 3, 4, 5]
    print(solution.countBadPairs(nums2))  # Expected output: 0

    # Test case 3: Một mảng với chỉ một phần tử, không thể có bất kỳ pair nào
    nums3 = [10]
    print(solution.countBadPairs(nums3))  # Expected output: 0

    # Test case 4: Mảng có các giá trị trùng nhau
    nums4 = [1, 1, 1, 1]
    print(solution.countBadPairs(nums4))  # Expected output: 0

    # Test case 5: Mảng với các giá trị ngẫu nhiên
    nums5 = [2, 3, 1, 4, 5]
    print(solution.countBadPairs(nums5))  # Expected output: a number based on logic

test()
