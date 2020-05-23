def sorted(arr,n):
    left = 0
    right = len(arr) - 1
    mid = 0

    while mid <= right:
        if arr[mid] ==0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left = left + 1
            mid = mid + 1
        elif arr[mid] ==1:
            mid = mid + 1
        else:
            arr[mid],arr[right] = arr[right],arr[mid]
            right = right -1

arr = [0,1,2,0,0,0,1,2,0,1,2,1]
n = len(arr)
sorted(arr,n)
print(arr)

