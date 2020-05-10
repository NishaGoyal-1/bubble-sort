arr1 = [1,12,15,26,38] #i
arr2 = [2,13,17,30,45] #j

def get_median(arr1,arr2):
    arr3 =[None]*(len(arr1) + len(arr2))
    i,j,k = 0,0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i = i + 1
            k = k + 1
        else:
            arr3[k] = arr2[j]
            j = j + 1
            k = k + 1
    while i < len(arr1):
        arr3[k] = arr1[i]
        i = i + 1
        k = k + 1

    while j < len(arr2):
        arr3[k] = arr2[j]
        j = j + 1
        k = k + 1
        pass

    #if len(arr3) is add
    print(arr3)
    mid = len(arr3)//2
    if len(arr3) %2 ==1:
        median = arr3[mid]
    else:
        median = (arr3[mid] + arr3[mid - 1])/2
    return median

result = get_median(arr1,arr2)
print(result)

(min(arr1[1],arr2[1]) + max(arr1[0], arr2[0]))/2

#arr1 = [15]
#arr2 = [17]

#16
def median(arr):
    mid = len(arr)//2
    if len(arr) % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid-1])/2

def get_median_v2(arr1,arr2):
    if len(arr1) == 1 and len(arr2) == 1:
        return (arr1[0] + arr2[0])/2
    if len(arr1) == 2 and len(arr2) == 2:
        return (min(arr1[1], arr2[1]) + max(arr1[0], arr2[0]))/2
    m1 = median(arr1)
    m2 = median(arr2)

    if m1 < m2:
        #second half of arr1
        #first half of arr2
        #get the mid element of array:
        #  odd,len //2
        #  even,len //2
        #arr1 = [1,12,15,26,38,40]#3
        #arr1 = [1,12,15,26,38]#2
        new_arr1 = arr1[len(arr1)//2:]
        new_arr2 = arr2[:(len(arr2)//2) + 1]
        return get_median_v2(new_arr1,new_arr2)
    else:
        #second half of arr2
        #first half of arr1
        new_arr1 = arr1[:(len(arr1) // 2) + 1]
        new_arr2 = arr2[len(arr2) // 2:]
        return get_median_v2(new_arr1, new_arr2)

# arr1 = [1,12,15,26,38] #15
# arr2 = [2,13,17,30,45] # 17
#
# arr1 = [1,2,3,4] #15
# arr2 = [5,6,7,8] #17

m1=15
m2=17

if m2 > m1:
    pass

# first half of arr2
# second half of arr1

arr1 = [15,26,38] #26
arr2 = [2,13,17] #13

arr1 = [15,26] #20.5
arr2 = [13,17] #15
result = get_median_v2(arr1,arr2)
print(result)