def search(arr, size):
    low=0
    high=len(arr)-1
    print(low)
    while (low +1 < high):
        mid = (low + high) // 2
        if (arr[low] - low) != (arr[mid] - mid):
            high = mid
        elif (arr[high] - high) != (arr[mid] - mid):
            low = mid
    return arr[low] + 1

arr=[1, 2, 3, 4, 6, 7, 8]
n=len(arr)
m=search(arr, n)
print("Missing Number: %d" % (m))
