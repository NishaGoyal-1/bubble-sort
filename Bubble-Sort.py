arr = [13,23,4,21,24,6]
arr = [1,3,12,34,21,-1,23]
arr = [-1,-8,-4,-6,-2,-5]
arr = [-1,0,1,5,4,3,2]
arr = [0,1,5,4,1,2,1,2,4]

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

#a, b = b, a
# print(a)
# print(b)

#array = [89,25,70,95,15,105,5]
#print(array)
# if array[0] > array[1]:
#     array[0], array[1]=array[1], array[0]
#
# if array[1] > array[2]:
#     array[1], array[2]=array[2], array[1]
#
# if array[2] > array[3]:
#     array[2], array[3]=array[3], array[2]
#
# print(array)
# for item in array:
#     print(item)
#
# array_1 = [89,25,70,95,15,105,5]
# array_2 = [25,36,32,31,29,26,20,30,36,34,24,28,37,10,36,28,39,28,27,20]
# def bubble_sort(array):
#     arr_len=len(array)
#     total_iteration = 0
#     for outer_index in range(arr_len - 1):
#         #print("outer_index:", outer_index)
#     for inner_index in range(arr_len - 1-outer_index):
#         total_iteration += 1
#         #print("inner_index:", inner_index)
#         if array[inner_index] > array[inner_index + 1]:
#             array[inner_index], array[inner_index + 1] = array[inner_index + 1], array[inner_index]
#     print(total_iteration)
#     print(array)
#
# def bubble_sort_v2(array):
#     arr_len = len(array)
#     total_iteration = 0
#     for outer_index in range(arr_len - 1):
#         #print("outer_index:", outer_index)
#         for inner_index in range(arr_len - 1):
#             total_iteration += 1
#             #print("inner_index:", inner_index)
#             if array[inner_index] > array[inner_index + 1]:
#                 array[inner_index], array[inner_index + 1] = array[inner_index + 1], array[inner_index]
#     print(total_iteration)
#     print(array)
#
# bubble_sort(array_1)
# bubble_sort_v2(array_1)
#
# bubble_sort(array_2)
# bubble_sort_v2(array_2)
#
#
