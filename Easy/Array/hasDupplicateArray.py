def has_duplicates(arr):
    return len(arr) != len(set(arr))

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 2, 3, 4]
arr1.append(0)
print(arr1)
print(has_duplicates(arr1))
print(has_duplicates(arr2))