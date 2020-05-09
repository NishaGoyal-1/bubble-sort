arr = [5,6,7,1,2,3,4]
arr = [2,3,4,5,6,7,1]
arr = [1,2,3,4,5,6,7]
arr = [1,2,3,4,5,6,1]
arr = [2,3,4,5,6,1,2]
arr = [1,1,2,3,4,5,6]

#ascending
#arr = [6,7,1,2,3,4,5]

#desending
#arr = [4,3,2,1,7,6,5]

#arr = [1,1,1,1,1,1,1]
#ascending
#last < first
#second > first
#desending
#last > first
#second < first

def find_min_in_ascending_sorted_rotated(arr):
    ans_index = 0
    if arr[0] < arr[-1]:
        return ans_index
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            ans_index = i+1
            break
    return ans_index
minimum = find_min_in_ascending_sorted_rotated(arr)
print(arr[minimum])

