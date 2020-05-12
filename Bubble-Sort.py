
arr = [13,23,4,21,24,6]

def bubble_sort(arr):
    iteration =0
    for i in range(0,len(arr)-1):#outer index
        for j in range(0,len(arr)-1-i):#inner index
            iteration +=1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(iteration)
    print(arr)

bubble_sort(arr)