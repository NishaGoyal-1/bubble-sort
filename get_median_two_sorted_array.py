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

#(min(arr1[1],arr2[1]) + max(arr1[0], arr2[0]))/2

#arr1 = [15]
#arr2 = [17]

#16
# def median(arr):
#     mid = len(arr)//2
#     if len(arr) % 2 == 1:
#         return arr[mid]
#     else:
#         return (arr[mid] + arr[mid-1])/2
#
# def get_median_v2(arr1,arr2):
#     if n ==1:
#         return (arr1[0] + arr2[0])/2
#     if n ==2:
#         return (min(arr1[1], arr2[1]) + max(arr1[0], arr2[0]))/2

#     m1 = median(arr1)
#     m2 = median(arr2)
#
#     if m1 > m2:
#
#         if n %2 ==0:
#             #n =6
#             #0:4(0,1,2,3),2:6(2,3,4,5)
#             return get_median_v2(arr1[:(n//2) + 1], arr2[(n//2)-1:], (n//2)+1)
#         else: #m1 < m2
#             #n=5,n/2=2,0.3(0,1,2)
#             #2:5 (2,3,4)
#             return  get_median_v2(arr1[:(n//2)+1], arr2[(n//2):], (n//2)+1)
#
#     else:
#         if n % 2 ==0:
#             return get_median_v2(arr1[(n//2-1):], arr2[:(n//2+1)], (n//2)+1)
#         else:
#             return get_median_v2(arr1[(n//2):], arr2[:(n//2)+1], (n//2)+1)
#
# arr1 = [1,12,15,26,38] # 15
# arr2 = [2,13,17,30,45] # 17

# arr1 = [1,12,15,26,38,65] #(15+25)/2
# arr2 = [2,13,17,30,45,98] #17

# arr1 = [1,2,3,4] #15
# arr2 = [5,6,7,8] #17

#m1=15
#m2=17

# if m2 > m1:
#     pass

# first half of arr2
# second half of arr1

# arr1 = [15,26,38] #26
# arr2 = [2,13,17] #13
#
# arr1 = [15,26] #20.5
# arr2 = [13,17] #15

# result = get_median(arr1,arr2)
# print(result)
#
# n = len(arr1)
#
# result = get_median_v2(arr1,arr2,n)
# print(result)

#arr1 = [1,12,15,25,38,65] #20
#arr2 = [2,13,17,30,45,98] #25

#[25,38,65]
#[2,13,17]

# arr1 =[15,25,38,65] #31.5
# arr2 = [2,13,17,33] #15
#
# arr1 = [15,25,38] #25
# arr2 = [13,17,33] #17
#
# arr1 = [15,25] #15
# arr2 = [17,33] #17
#
# arr1 = [1,12,15,26,38] #15
# arr2 = [2,13,17,30,45] #17
#
# def get_median_v3(arr1,arr2):
#
#     pass

#i = 0
#j = 0
#total_elements = 10
#count = 0
#4,5

#total_elements//2 #5 +1

#i =1, j =0, count=1
#j =1, i =1, count=2