class Arrray:
    def __init__(self, arr):
        self.arr = arr
    
    def find_max(self):
        if not self.arr:
            return None
        max_value = self.arr[0]
        for num in self.arr:
            if num > max_value:
                max_value = num
        return max_value

    def find_index(self, target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1

    # Kiem tra mang co doi xung khong
    def is_palindrome(self):
        left , right = 0, len(self.arr) - 1
        while left < right:
            if self.arr[left] != self.arr[right]:
                return False
            left += 1
            right -= 1
        return True

    def sort_ascending(self):
        self.arr.sort()

    def sort_descending(self):
        self.arr.sort(reverse=True)

arr = Arrray([5, 2, 9, 1, 7, 3])
max_value = arr.find_max()
print("Maximum value in the array:", max_value)

target_value = 7
index = arr.find_index(target_value)
print("Index of target value:", index)

is_palindrome = arr.is_palindrome()
print("Is the array palindrome:", is_palindrome)

arr.sort_ascending()
print("Sorted array in ascending order:", arr.arr)

arr.sort_descending()
print("Sorted array in descending order:", arr.arr)