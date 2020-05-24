# arr = [2,4,8,10,12,14,16]
# arr = [1, 6, 11, 16, 21, 31, 36]
# arr = [-1,-4,-8,-16,-20,-24,-28]
# arr = [10,15,20,30,35,40,45]
# arr = [60,54,48,42,30,24,18]
arr = [20,30,50,60,70,80,90]
left = 0
right= 6
diff = (arr[right] - arr[left])/len(arr)
print(diff)
while right >= left:
    if arr[left+1] == arr[left] + diff:
        left = left + 1
    else:
        print(arr[left] + diff)
        break

    if arr[right-1] == arr[right] - diff:
        right = right - 1
    else:
        print(arr[right] - diff)
        break
print(arr)

