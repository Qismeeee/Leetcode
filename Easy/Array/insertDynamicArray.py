def insert_dynamic(arr, value, position):
    arr.append(0) # Mở rộng mảng
    for i in range(len(arr) - 1, position, -1):
        arr[i] = arr[i - 1]
    arr[position] = value

arr = [1,2,3,4,5]
insert_dynamic(arr, 6, 2)
print(arr)